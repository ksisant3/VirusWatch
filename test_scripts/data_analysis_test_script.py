import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file = 'D:\Data analyzation folder\Excell_data_files\2019 nCoV wastewater 07152020_results_AlteredForCapstone.xlsx'

data = pd.read_excel(excel_file, sheet_name='sheet1')

selectedData = data.groupby(['Sample Name', 'Target Name', 'CT', 'CT Mean'])

selectedData.plot(xlabel = 'Target_Mean', ylabel = 'Particle_Density')

print(selectedData)

plot.xticks(np.arange(0, x_max, 250), rotation=45)
plot.show()


#####################################################################################################
#R script to initially be translated in python for functionality testing. Here for reference. 

# library(shiny)
# library(xlsx)
# library(dplyr)
# # Demo program for capstone
# # ========================================================================
# data <- read.xlsx("Demo_data.xlsx", sheetIndex = 1)
# selectedData <- data %>% select(Sample.Name, Target.Name, CT, Ct.Mean)
# selectedData <- selectedData %>% mutate(Particle_Density = "NA")
# N1Target <- selectedData %>% filter(Target.Name == "N1")
# N2Target <- selectedData %>% filter(Target.Name == "N2")

# N1Target$Particle_Density[which(
  # (N1Target$Sample.Name %in% "PTC 1:10"))] <- 20000
# N1Target$Particle_Density[which(
  # (N1Target$Sample.Name %in% "PTC 1:100"))] <- 2000
# N1Target$Particle_Density[which(
  # (N1Target$Sample.Name %in% "PTC 1:1000"))] <- 200

# N2Target$Particle_Density[which(
  # (N2Target$Sample.Name %in% "PTC 1:10"))] <- 20000
# N2Target$Particle_Density[which(
  # (N2Target$Sample.Name %in% "PTC 1:100"))] <- 2000
# N2Target$Particle_Density[which(
  # (N2Target$Sample.Name %in% "PTC 1:1000"))] <- 200

# suppressWarnings(plot(N1Target$Ct.Mean, N1Target$Particle_Density, 
                      # type = "l", xlab = "Target Mean", ylab = "Particle Density"))
# suppressWarnings(plot(N2Target$Ct.Mean, N2Target$Particle_Density, 
                      # type = "l", xlab = "Target Mean", ylab = "Particle Density"))
# print(N1Target)
# print(N2Target)

# # for(i in N1Target$Sample.Name){
# #   if(grepl("1:1000", i, fixed = TRUE)){
# #     N1Target$Particle_Density[which((N1Target))] <- 200
# #   }
# #   else if(grepl("1:100", i, fixed = TRUE)){
# #     N1Target$Particle_Density[i] <- 2000
# #   }
# #   else if(grepl("1:10", i, fixed = TRUE)){
# #     N1Target$Particle_Density[i] <- 20000
# #   }
# # }

