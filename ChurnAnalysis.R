# Sandbox for Churn Data

# Load the file for analysis
file <- "./ChurnData.csv";
churnData = read.csv(file);
summary(churnData);
head(churnData);
tail(churnData);

plot(churnData$Area_Code);

