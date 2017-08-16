#loading library
require("ggplot2")

# selecting the current directory
setwd("/Users/tassiovale/Dropbox/PhD Thesis/spltrac/experiment/results/")

# read csv file
data <- read.csv("2017-08-11_10h56m_output.csv")

chart <- ggplot(data=data, aes(x=recall, y=precision, group=method, colour=method)) +
    geom_line() +
    geom_point(aes(shape=method)) +
    ggtitle("Precision x recall") +
    labs(x="Recall", y="Precision") +
    scale_fill_discrete(name="IR method")

ggsave("2017-08-11_10h56m_precisionrecall_chart.eps")