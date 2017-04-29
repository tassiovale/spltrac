# selecting the current directory
setwd("<directory>")

# read csv file
data <- read.csv("<output_file_name>")

cat("\n\n\n")
print("ANOVA - F-MEASURE")
aov_results = aov(fmeasure ~ method, data=data)
print(summary(aov_results))
pvalue = summary(aov_results)[[1]][["Pr(>F)"]][1]
if(pvalue <= 0.05){
    cat("\n\n")
    print("p-value OK. Null hypothesis rejected.")
    print("Applying pairwise t-Student:")
    pairwise_results = pairwise.t.test(data$fmeasure, data$method, p.adjust="bonferroni")
    print(pairwise_results)
    cat("\n\n")
    print("Applying Tukey's Honest Significance Test:")
    tukey_results = TukeyHSD(aov_results, conf.level = 0.95)
    print(tukey_results)
}

cat("\n\n\n")
print("ANOVA - PRECISION")
aov_results = aov(precision ~ method, data=data)
print(summary(aov_results))
pvalue = summary(aov_results)[[1]][["Pr(>F)"]][1]
if(pvalue <= 0.05){
    cat("\n\n")
    print("p-value OK. Null hypothesis rejected.")
    print("Applying pairwise t-Student:")
    pairwise_results = pairwise.t.test(data$precision, data$method, p.adjust="bonferroni")
    print(pairwise_results)
    cat("\n\n")
    print("Applying Tukey's Honest Significance Test:")
    tukey_results = TukeyHSD(aov_results, conf.level = 0.95)
    print(tukey_results)
}

cat("\n\n\n")
print("ANOVA - RECALL")
aov_results = aov(recall ~ method, data=data)
print(summary(aov_results))
pvalue = summary(aov_results)[[1]][["Pr(>F)"]][1]
if(pvalue <= 0.05){
    cat("\n\n")
    print("p-value OK. Null hypothesis rejected.")
    print("Applying pairwise t-Student:")
    pairwise_results = pairwise.t.test(data$recall, data$method, p.adjust="bonferroni")
    print(pairwise_results)
    cat("\n\n")
    print("Applying Tukey's Honest Significance Test:")
    tukey_results = TukeyHSD(aov_results, conf.level = 0.95)
    print(tukey_results)
}

cat("\n\n\n")
print("ANOVA - PERFORMANCE")
aov_results = aov(performance ~ method, data=data)
print(summary(aov_results))
pvalue = summary(aov_results)[[1]][["Pr(>F)"]][1]
if(pvalue <= 0.05){
    cat("\n\n")
    print("p-value OK. Null hypothesis rejected.")
    print("Applying pairwise t-Student:")
    pairwise_results = pairwise.t.test(data$performance, data$method, p.adjust="bonferroni")
    print(pairwise_results)
    cat("\n\n")
    print("Applying Tukey's Honest Significance Test:")
    tukey_results = TukeyHSD(aov_results, conf.level = 0.95)
    print(tukey_results)
}