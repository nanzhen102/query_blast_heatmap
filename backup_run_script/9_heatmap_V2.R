data <- read.csv('/Users/nanzhen/Desktop/GitHub/Heatmap_axis_reorder/75cov_50aa_proportation_Liquoricoccoides_plus_337genomes_etc_reorder_full_2.csv', header = TRUE)

data$Genus<-factor(data$Genus, levels=data$Genus[33:1])

# install.packages("reshape2") 
# install.packages("ggplot2")

library(reshape2)
melted_cormat <- melt(data)
library(ggplot2)

plot1 <- ggplot(melted_cormat, aes(x=variable, y=Genus, fill=value)) + geom_tile() + scale_fill_gradient2(low = "white", high = "#FF0000", space = "Lab", name = "Proportion\nof genes\nin genera") + theme(axis.text.x = element_text(angle = 45, vjust = 1, size = 30, hjust = 1), axis.text.y = element_text(face = "italic", size = 30), legend.text = element_text(size = 30), legend.key.size = unit(2, 'cm'), legend.title = element_text(size = 30)) + coord_fixed()
plot2 <- plot1 + xlab("Genes") + ylab("Genera") + theme(axis.title.x=element_text(size=30), axis.title.y=element_text(size=30))
# plot2

ggsave("dddd.png", units="in", width=30, height=40, dpi=300)

