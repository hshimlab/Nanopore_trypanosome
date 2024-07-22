#library(ggpattern)
library(ggplot2)
library(hrbrthemes)

df = data.frame(
  name=c("TrypOnly","TrypBlood_1","TrypBlood_Control","TrypBlood_2","Feces_Control","Feces_Infected"),
  val=c(98.61, 97.08, 0.03, 26.81, 0.01, 0.01)
)

ggplot(df, aes(x=name, y=val, fill=name)) +
  geom_bar(stat="identity", alpha=.6, width=.4) +
  scale_fill_grey(start=0, end=0.8) +  # start and end define the range of grays
  theme_bw()


dev.off()