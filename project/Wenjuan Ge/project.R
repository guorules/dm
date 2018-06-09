data<-read.csv("coinUSD.csv", header = TRUE)
data
summary(data)
barplot(data$V2, data$V3, main = "coinUSD", xlab = "price", ylab = "volume")

data2<-read.csv("abucoinsEUR.csv", header = TRUE)
data2
summary(data2)
barplot(data2$V2, data2$V3, main = "abucoinsEUR", xlab = "price", ylab = "volume")