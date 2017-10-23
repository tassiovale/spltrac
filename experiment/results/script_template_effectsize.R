#loading library - it requires the installation of the effsize package
require("effsize")

# selecting the current directory
setwd("/Users/tassiovale/Downloads/spltrac")

# read csv file
dataspl <- read.csv("data-spl-withLSI.csv")
datapreprocessor <- read.csv("data_preprocessor.csv")

dataspl_cv = dataspl[dataspl$Method=='Classic vector model',]
datapreprocessor_cv = datapreprocessor[datapreprocessor$Method=='Classic vector model',]

dataspl_eb = dataspl[dataspl$Method=='Extended boolean',]
datapreprocessor_eb = datapreprocessor[datapreprocessor$Method=='Extended boolean',]

dataspl_nn = dataspl[dataspl$Method=='Neural networks',]
datapreprocessor_nn = datapreprocessor[datapreprocessor$Method=='Neural networks',]

dataspl_bm25 = dataspl[dataspl$Method=='BM25',]
datapreprocessor_bm25 = datapreprocessor[datapreprocessor$Method=='BM25',]

cat("======= PRECISION =======")

cat("\n\nGeneral")

result = cohen.d(dataspl$precision,datapreprocessor$precision,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nClassic vector")

result = cohen.d(dataspl_cv$precision,datapreprocessor_cv$precision,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nExtended boolean")

result = cohen.d(dataspl_eb$precision,datapreprocessor_eb$precision,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nNeural networks")

result = cohen.d(dataspl_nn$precision,datapreprocessor_nn$precision,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nBM25")

result = cohen.d(dataspl_bm25$precision,datapreprocessor_bm25$precision,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\n\n\n======= RECALL =======")

cat("\n\nGeneral")

result = cohen.d(dataspl$recall,datapreprocessor$recall,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nClassic vector")

result = cohen.d(dataspl_cv$recall,datapreprocessor_cv$recall,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nExtended boolean")

result = cohen.d(dataspl_eb$recall,datapreprocessor_eb$recall,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nNeural networks")

result = cohen.d(dataspl_nn$recall,datapreprocessor_nn$recall,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nBM25")

result = cohen.d(dataspl_bm25$recall,datapreprocessor_bm25$recall,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\n\n\n======= F-MEASURE =======")

cat("\n\nGeneral")

result = cohen.d(dataspl$fmeasure,datapreprocessor$fmeasure,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nClassic vector")

result = cohen.d(dataspl_cv$fmeasure,datapreprocessor_cv$fmeasure,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nExtended boolean")

result = cohen.d(dataspl_eb$fmeasure,datapreprocessor_eb$fmeasure,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nNeural networks")

result = cohen.d(dataspl_nn$fmeasure,datapreprocessor_nn$fmeasure,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nBM25")

result = cohen.d(dataspl_bm25$fmeasure,datapreprocessor_bm25$fmeasure,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\n\n\n======= TIME BEHAVIOR =======")

cat("\n\nGeneral")

result = cohen.d(dataspl$performance,datapreprocessor$performance,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nClassic vector")

result = cohen.d(dataspl_cv$performance,datapreprocessor_cv$performance,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nExtended boolean")

result = cohen.d(dataspl_eb$performance,datapreprocessor_eb$performance,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nNeural networks")

result = cohen.d(dataspl_nn$performance,datapreprocessor_nn$performance,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))

cat("\n\nBM25")

result = cohen.d(dataspl_bm25$performance,datapreprocessor_bm25$performance,paired=FALSE,hedges.correction=TRUE)
print(result)
print(summary(result))
