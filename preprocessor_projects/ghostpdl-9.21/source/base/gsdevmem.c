/* Copyright (C) 2001-2012 Artifex Software, Inc.
   All Rights Reserved.

   This software is provided AS-IS with no warranty, either express or
   implied.

   This software is distributed under license and may not be copied,
   modified or distributed except as expressly authorized under the terms
   of the license contained in the file LICENSE in this distribution.

   Refer to licensing information at http://www.artifex.com or contact
   Artifex Software, Inc.,  7 Mt. Lassen Drive - Suite A-134, San Rafael,
   CA  94903, U.S.A., +1(415)492-9861, for further information.
*/


/* Memory device creation for Ghostscript library */
#include "math_.h"		/* for fabs */
#include "memory_.h"
#include "gx.h"
#include "gserrors.h"
#include "gsdevice.h"		/* for prototypes */
#include "gxarith.h"
#include "gxdevice.h"
#include "gxdevmem.h"

/* Make a memory (image) device. */
/* If colors_size = -16, -24, or -32, this is a true-color device; */
/* otherwise, colors_size is the size of the palette in bytes */
/* (2^N for gray scale, 3*2^N for RGB color). */
/* We separate device allocation and initialization at customer request. */
int
gs_initialize_wordimagedevice(gx_device_memory * new_dev, const gs_matrix * pmat,
              uint width, uint height, const byte * colors, int colors_size,
                    bool word_oriented, bool page_device, gs_memory_t * mem)
{
    const gx_device_memory *proto_dev;
    int palette_count = colors_size;
    int num_components = 1;
    int pcount;
    int bits_per_pixel;
    float x_pixels_per_unit, y_pixels_per_unit;
    byte palette[256 * 3];
    bool has_color;

    switch (colors_size) {
        case 3 * 2:
            palette_count = 2;
            num_components = 3;
            /* fall through */
        case 2:
            bits_per_pixel = 1;
            break;
        case 3 * 4:
            palette_count = 4;
            num_components = 3;
            /* fall through */
        case 4:
            bits_per_pixel = 2;
            break;
        case 3 * 16:
            palette_count = 16;
            num_components = 3;
            /* fall through */
        case 16:
            bits_per_pixel = 4;
            break;
        case 3 * 256:
            palette_count = 256;
            num_components = 3;
            /* fall through */
        case 256:
            bits_per_pixel = 8;
            break;
        case -16:
            bits_per_pixel = 16;
            palette_count = 0;
            break;
        case -24:
            bits_per_pixel = 24;
            palette_count = 0;
            break;
        case -32:
            bits_per_pixel = 32;
            palette_count = 0;
            break;
        default:
            return_error(gs_error_rangecheck);
    }
    proto_dev = (word_oriented ?
                 gdev_mem_word_device_for_bits(bits_per_pixel) :
                 gdev_mem_device_for_bits(bits_per_pixel));
    if (proto_dev == 0)		/* no suitable device */
        return_error(gs_error_rangecheck);
    pcount = palette_count * 3;
    /* Check to make sure the palette contains white and black, */
    /* and, if it has any colors, the six primaries. */
    if (bits_per_pixel <= 8) {
        const byte *p;
        byte *q;
        int primary_mask = 0;
        int i;

        has_color = false;
        for (i = 0, p = colors, q = palette;
             i < palette_count; i++, q += 3
            ) {
            int mask = 1;

            switch (num_components) {
                case 1:	/* gray */
                    q[0] = q[1] = q[2] = *p++;
                    break;
                default /* case 3 */ :		/* RGB */
                    q[0] = p[0], q[1] = p[1], q[2] = p[2];
                    p += 3;
            }
#define shift_mask(b,n)\
  switch ( b ) { case 0xff: mask <<= n; case 0: break; default: mask = 0; }
            shift_mask(q[0], 4);
            shift_mask(q[1], 2);
            shift_mask(q[2], 1);
#undef shift_mask
            primary_mask |= mask;
            if (q[0] != q[1] || q[0] != q[2])
                has_color = true;
        }
        switch (primary_mask) {
            case 129:		/* just black and white */
                if (has_color)	/* color but no primaries */
                    return_error(gs_error_rangecheck);
            case 255:		/* full color */
                break;
            default:
                return_error(gs_error_rangecheck);
        }
    } else
        has_color = true;
    /*
     * The initial transformation matrix must map 1 user unit to
     * 1/72".  Let W and H be the width and height in pixels, and
     * assume the initial matrix is of the form [A 0 0 B X Y].
     * Then the size of the image in user units is (W/|A|,H/|B|),
     * hence the size in inches is ((W/|A|)/72,(H/|B|)/72), so
     * the number of pixels per inch is
     * (W/((W/|A|)/72),H/((H/|B|)/72)), or (|A|*72,|B|*72).
     * Similarly, if the initial matrix is [0 A B 0 X Y] for a 90
     * or 270 degree rotation, the size of the image in user
     * units is (W/|B|,H/|A|), so the pixels per inch are
     * (|B|*72,|A|*72).  We forbid non-orthogonal transformation
     * matrices.
     */
    if (is_fzero2(pmat->xy, pmat->yx))
        x_pixels_per_unit = pmat->xx, y_pixels_per_unit = pmat->yy;
    else if (is_fzero2(pmat->xx, pmat->yy))
        x_pixels_per_unit = pmat->yx, y_pixels_per_unit = pmat->xy;
    else
        return_error(gs_error_undefinedresult);
    /* All checks done, initialize the device. */
    if (bits_per_pixel == 1) {
        /* Determine the polarity from the palette. */
        gs_make_mem_device(new_dev, proto_dev, mem,
                           (page_device ? 1 : -1), 0);
        /* This is somewhat bogus, but does the right thing */
        /* in the only cases we care about. */
        gdev_mem_mono_set_inverted(new_dev,
                               (palette[0] | palette[1] | palette[2]) != 0);
    } else {
        byte *dev_palette = gs_alloc_string(mem, pcount,
                                            "gs_makeimagedevice(palette)");

        if (dev_palette == 0)
            return_error(gs_error_VMerror);
        gs_make_mem_device(new_dev, proto_dev, mem,
                           (page_device ? 1 : -1), 0);
        new_dev->palette.size = pcount;
        new_dev->palette.data = dev_palette;
        memcpy(dev_palette, palette, pcount);
        if (!has_color) {
            new_dev->color_info.num_components = 1;
            new_dev->color_info.max_color = 0;
            new_dev->color_info.dither_colors = 0;
            new_dev->color_info.gray_index = 0;
        }
    }
    /* Memory defice is always initialised as an internal device but */
    /* this is an external device */
    new_dev->retained = true;
    rc_init(new_dev, new_dev->memory, 1);

    new_dev->initial_matrix = *pmat;
    new_dev->HWResolution[0] = fabs(x_pixels_per_unit) * 72;
    new_dev->HWResolution[1] = fabs(y_pixels_per_unit) * 72;
    gx_device_set_width_height((gx_device *) new_dev, width, height);
    /* Set the ImagingBBox so we get a correct clipping region. */
    {
        gs_rect bbox;

        bbox.p.x = 0;
        bbox.p.y = 0;
        bbox.q.x = width;
        bbox.q.y = height;
        gs_bbox_transform_inverse(&bbox, pmat, &bbox);
        new_dev->ImagingBBox[0] = bbox.p.x;
        new_dev->ImagingBBox[1] = bbox.p.y;
        new_dev->ImagingBBox[2] = bbox.q.x;
        new_dev->ImagingBBox[3] = bbox.q.y;
        new_dev->ImagingBBox_set = true;
    }
    /* The bitmap will be allocated when the device is opened. */
    new_dev->is_open = false;
    new_dev->bitmap_memory = mem;
    return 0;
}

int
gs_makewordimagedevice(gx_device ** pnew_dev, const gs_matrix * pmat,
               uint width, uint height, const byte * colors, int num_colors,
                    bool word_oriented, bool page_device, gs_memory_t * mem)
{
    int code;
    gx_device_memory *pnew =
    gs_alloc_struct(mem, gx_device_memory, &st_device_memory,
                    "gs_makeimagedevice(device)");

    if (pnew == 0)
        return_error(gs_error_VMerror);

    /* Bug #697450 "Null pointer dereference in gx_device_finalize()"
     * If we have incorrect data passed to gs_initialise_wordimagedevice() then the
     * initialisation will fail, crucially it will fail *before* it calls
     * gs_make_mem_device() which initialises the device. This means that the
     * icc_struct member will be uninitialsed, but the device finalise method
     * will unconditionally free that memory. Since its a garbage pointer, bad things happen.
     * Apparently we do still need makeimagedevice to be available from
     * PostScript, so in here just zero the device memory, which means that
     * the finalise routine won't have a problem.
     */
    memset(pnew, 0x00, st_device_memory.ssize);
    code = gs_initialize_wordimagedevice(pnew, pmat, width, height,
                                         colors, num_colors, word_oriented,
                                         page_device, mem);
    if (code < 0) {
        gs_free_object(mem, pnew, "gs_makeimagedevice(device)");
        return code;
    }
    *pnew_dev = (gx_device *) pnew;
    return 0;
}