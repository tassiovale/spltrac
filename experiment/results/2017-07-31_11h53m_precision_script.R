#loading library
require("ggplot2")

# selecting the current directory
setwd("/home/user/tassiovale/spltrac/experiment/results/")

# read csv file
data <- read.csv("2017-07-31_11h53m_output.csv")

chart <- ggplot(data=data, aes(x=method, y=precision, fill=method)) +
    geom_boxplot() +
    theme_minimal() +
    ggtitle("Precision per method") +
    labs(x="IR method", y="Precision") +
    scale_fill_discrete(guide=FALSE)

ggsave("2017-07-31_11h53m_precision_chart.eps")