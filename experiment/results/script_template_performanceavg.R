#loading library
require("ggplot2")

# selecting the current directory
setwd("<directory>")

# read csv file
data <- read.csv("<output_file_name>")

chart <- ggplot(data=data, aes(x=method, y=performance, fill=method)) +
    geom_boxplot() +
    theme_minimal() +
    ggtitle("Performance results") +
    labs(x="IR method", y="Performance (in seconds)") +
    scale_fill_discrete(guide=FALSE)

ggsave(paste("<pdf_image_file_name>", '.pdf', sep=""), chart)