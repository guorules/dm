# input the path, where to save the output of csv file
setwd("/Users/SallyGwj./Desktop")
getwd


#download every files from web page
con1 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                       "1coinUSD.csv.gz", sep="")))
txt <- readLines(con1)
coinUSD <- read.csv(textConnection(txt), header = F)
write.csv(coinUSD, file = "coinUSD.csv")


#abucoinsEUR
con2 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                        "abucoinsEUR.csv.gz", sep="")))
txt <- readLines(con2)
abucoinsEUR <- read.csv(textConnection(txt), header = F)
write.csv(abucoinsEUR, file = "abucoinsEUR.csv")

#abucoinsPLN
con3 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                        "abucoinsPLN.csv.gz", sep="")))
txt <- readLines(con3)
abucoinsPLN <- read.csv(textConnection(txt), header = F)
write.csv(abucoinsPLN, file = "abucoinsPLN.csv")

#abucoinsUSD
con4 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                        "abucoinsUSD.csv.gz", sep="")))
txt <- readLines(con4)
abucoinsUSD <- read.csv(textConnection(txt), header = F)
write.csv(abucoinsUSD, file = "abucoinsUSD.csv")

#allcoinUSD
con5 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                        "allcoinUSD.csv.gz", sep="")))
txt <- readLines(con5)
allcoinUSD <- read.csv(textConnection(txt), header = F)
write.csv(allcoinUSD, file = "allcoinUSD.csv")

#anxhkAUD
con6 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                        "anxhkAUD.csv.gz", sep="")))
txt <- readLines(con6)
anxhkAUD <- read.csv(textConnection(txt), header = F)
write.csv(anxhkAUD, file = "anxhkAUD.csv")

#anxhkCAD
con7 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                        "anxhkCAD.csv.gz", sep="")))
txt <- readLines(con7)
anxhkCAD <- read.csv(textConnection(txt), header = F)
write.csv(anxhkCAD, file = "anxhkCAD.csv")

#anxhkCHF
con8 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                        "anxhkCHF.csv.gz", sep="")))
txt <- readLines(con8)
anxhkCHF <- read.csv(textConnection(txt), header = F)
write.csv(anxhkCHF, file = "anxhkCHF.csv")

#anxhkCNY
con9 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                        "anxhkCNY.csv.gz", sep="")))
txt <- readLines(con9)
anxhkCNY <- read.csv(textConnection(txt), header = F)
write.csv(anxhkCNY, file = "anxhkCNY.csv")

#anxhkEUR
con10 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                        "anxhkEUR.csv.gz", sep="")))
txt <- readLines(con10)
anxhkEUR <- read.csv(textConnection(txt), header = F)
write.csv(anxhkEUR, file = "anxhkEUR.csv")

#anxhkGBP
con11 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                        "anxhkGBP.csv.gz", sep="")))
txt <- readLines(con11)
anxhkGBP <- read.csv(textConnection(txt), header = F)
write.csv(anxhkGBP, file = "anxhkGBP.csv")

#anxhkHKD
con12 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                         "anxhkHKD.csv.gz", sep="")))
txt <- readLines(con12)
anxhkHKD <- read.csv(textConnection(txt), header = F)
write.csv(anxhkHKD, file = "anxhkHKD.csv")

#anxhkJPY
con13 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                         "anxhkJPY.csv.gz", sep="")))
txt <- readLines(con13)
anxhkJPY <- read.csv(textConnection(txt), header = F)
write.csv(anxhkJPY, file = "anxhkJPY.csv")

#anxhkNZD
con14 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                         "anxhkNZD.csv.gz", sep="")))
txt <- readLines(con14)
anxhkNZD <- read.csv(textConnection(txt), header = F)
write.csv(anxhkNZD, file = "anxhkNZD.csv")

#anxhkSGD
con15 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                         "anxhkSGD.csv.gz", sep="")))
txt <- readLines(con15)
anxhkSGD <- read.csv(textConnection(txt), header = F)
write.csv(anxhkSGD, file = "anxhkSGD.csv")

#anxhkUSD
con16 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                         "anxhkUSD.csv.gz", sep="")))
txt <- readLines(con16)
anxhkUSD <- read.csv(textConnection(txt), header = F)
write.csv(anxhkUSD, file = "anxhkUSD.csv")

#anxhkEUR
con17 <- gzcon(url(paste("http://api.bitcoincharts.com/v1/csv/",
                         "anxhkEUR.csv.gz", sep="")))
txt <- readLines(con17)
anxhkEUR <- read.csv(textConnection(txt), header = F)
write.csv(anxhkEUR, file = "anxhkEUR.csv")

# connect to unzip file...
