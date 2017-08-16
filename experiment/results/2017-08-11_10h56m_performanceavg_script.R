#loading library
require("ggplot2")

# selecting the current directory
setwd("/Users/tassiovale/Dropbox/PhD Thesis/spltrac/experiment/results/")

# read csv file
data <- read.csv("2017-08-11_10h56m_output.csv")

chart <- ggplot(data=data, aes(x=method, y=performance, fill=method)) +
    geom_boxplot() +
    theme_minimal() +
    ggtitle("Time behavior results") +
    labs(x="IR method", y="Time behavior (in seconds)") +
    scale_fill_discrete(guide=FALSE)

ggsave("2017-08-11_10h56m_performanceavg_chart.eps")