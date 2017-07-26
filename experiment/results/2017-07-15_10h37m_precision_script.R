#loading library
require("ggplot2")

# selecting the current directory
setwd("/Users/tassiovale/Dropbox/PhD Thesis/spltrac/experiment/results/")

# read csv file
data <- read.csv("2017-07-15_10h37m_output.csv")

chart <- ggplot(data=data, aes(x=method, y=precision, fill=method)) +
    geom_boxplot() +
    theme_minimal() +
    ggtitle("Precision per method") +
    labs(x="IR method", y="Precision") +
    scale_fill_discrete(guide=FALSE)

ggsave("2017-07-15_10h37m_precision_chart.eps")