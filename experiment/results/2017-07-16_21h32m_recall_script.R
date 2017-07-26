#loading library
require("ggplot2")

# selecting the current directory
setwd("/Users/tassiovale/Dropbox/PhD Thesis/spltrac/experiment/results/")

# read csv file
data <- read.csv("2017-07-16_21h32m_output.csv")

chart <- ggplot(data=data, aes(x=method, y=recall, fill=method)) +
    geom_boxplot() +
    theme_minimal() +
    ggtitle("Recall per method") +
    labs(x="IR method", y="Recall") +
    scale_fill_discrete(guide=FALSE)

ggsave("2017-07-16_21h32m_recall_chart.eps")