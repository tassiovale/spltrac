/* Dia -- an diagram creation/manipulation program
 * Copyright (C) 1998 Alexander Larsson
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 */
#ifndef INTERFACE_H
#define INTERFACE_H

#include "display.h"

#include "app_procs.h"

/* Integrated UI Constants */
#define  DIA_MAIN_WINDOW   "dia-main-window"
#define  DIA_MAIN_NOTEBOOK "dia-main-notebook"

void create_integrated_ui (void);

gboolean integrated_ui_toolbar_is_showing (void);
void     integrated_ui_toolbar_show (gboolean show);

void     integrated_ui_statusbar_show (gboolean show);

gboolean integrated_ui_layer_view_is_showing (void);
void     integrated_ui_layer_view_show (gboolean show);

int is_integrated_ui (void);

void create_display_shell(DDisplay *ddisp,
			  int width, int height,
			  char *title, int use_mbar);

void create_toolbox (void);
void toolbox_show(void);
void toolbox_hide(void);

GtkWidget *interface_get_toolbox_shell(void);

void create_integrated_ui (void);

void create_sheets(GtkWidget *parent);
extern GtkWidget *modify_tool_button;

void view_zoom_set (float zoom_factor); /* zoom_factor is 10 * percentage */

void fill_sheet_menu(void);

void close_notebook_page_callback (GtkButton *button, gpointer user_data);

#endif /* INTERFACE_H */
