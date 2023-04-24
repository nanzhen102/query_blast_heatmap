data <- read.csv('/Volumes/USB/1_phd_2020/5_doctoral_program/0.1_type_strain_tree/5_weissella_tree_0921/4_add_two_new_genomes/3_query_blast/2_multi_query/75cov_50aa_proportation_Liquoricoccoides_plus_337genomes_etc_fullname.csv', header = TRUE)

data$Genus<-factor(data$Genus, levels=data$Genus[33:1])

library(reshape2)
melted_cormat <- melt(data)
library(ggplot2)

plot1 <- ggplot(melted_cormat, aes(x=variable, y=Genus, fill=value)) + geom_tile() + scale_fill_gradient2(low = "white", high = "#FF0000", space = "Lab", name = "Proportion\nof genes\nin genera") + theme(axis.text.x = element_text(angle = 45, vjust = 1, size = 25, hjust = 1), axis.text.y = element_text(face = "italic", size = 25)) + coord_fixed()
plot2 <- plot1 + xlab("Genes") + ylab("Genera")
plot2

