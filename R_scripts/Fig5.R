############ barplot
# Create the data for the chart 
GFG_ID   <- c(1:5) 
GFG_Sal  <- c(98.61, 97.08, 0.03, 26.81, 0.01, 0.01) 
GFG_Name <- c("TrypOnly","TrypBlood_1","TrypBlood_Control","TrypBlood_2","Feces_Control","Feces_Infected") 
X <- data.frame(GFG_ID,GFG_Name,GFG_Sal) 
X 

# Give the chart file a name 
png(file = "Fig5.png", width = 800, height = 400) 

# Plot the bar chart  
barplot(GFG_Sal,names.arg=GFG_Name,xlab="Sample", 
        ylab="",col=gray.colors(6, start=0, end=0.9), ylim=c(0,100)) 

# Save the file 
dev.off()

########### ggplot

#library(ggpattern)
library(ggplot2)
library(hrbrthemes)

df = data.frame( ID=c(1:6)
                 Sample=c("TrypOnly","TrypBlood_1","TrypBlood_Control","TrypBlood_2","Feces_Control","Feces_Infected"),
                 Percentage=c(98.61, 97.08, 0.03, 26.81, 0.01, 0.01)
)

ggplot(df, aes(x=Sample, y=Percentage, fill=Sample)) +
  geom_bar(stat="identity", alpha=.6, width=.4) +
  scale_fill_grey(start=0, end=0.8) +  # start and end define the range of grays
  theme_bw()


dev.off()
print(plot(1))
