data <- read.csv('/Users/nanzhen/Documents/GitHub/query_blast_heatmap/all_prot_query_screened_header_40ide_70cov_positive_negative_species_matched_grouped_ordered_percentage.csv', header = TRUE)

data$Genus<-factor(data$Genus, levels=data$Genus[33:1]) # be carefule, if it's Genus or genus in the csv file.

# install.packages("reshape2") 
# install.packages("ggplot2")

library(reshape2)
melted_cormat <- melt(data)
library(ggplot2)

# for large dataset
# plot1 <- ggplot(melted_cormat, aes(x=variable, y=Genus, fill=value)) + geom_tile() + scale_fill_gradient2(low = "white", high = "#FF0000", space = "Lab", name = "Proportion\nof genes\nin genera") + theme(axis.text.x = element_text(angle = 45, vjust = 1, size = 30, hjust = 1), axis.text.y = element_text(face = "italic", size = 30), legend.text = element_text(size = 30), legend.key.size = unit(2, 'cm'), legend.title = element_text(size = 30)) + coord_fixed()

plot1 <- ggplot(melted_cormat, aes(x=variable, y=Genus, fill=value)) + geom_tile() + scale_fill_gradient2(low = "white", high = "#FF0000", space = "Lab", name = "Proportion\nof genes\nin genera\n") + theme(axis.text.x = element_text(angle = 90, vjust = 1, size = 40, hjust = 1), axis.text.y = element_text(face = "italic", size = 40), legend.text = element_text(size = 40), legend.key.size = unit(2, 'cm'), legend.title = element_text(size = 40)) + coord_fixed()

plot2 <- plot1 + xlab("Genes") + ylab("Genera") + theme(axis.title.x=element_text(size=40), axis.title.y=element_text(size=40))
# plot2

ggsave("dddd3.png", units="in", width=40, height=48, dpi=300)

