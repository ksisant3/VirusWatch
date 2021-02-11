import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

excel_file = 'D:\School_class_folders\Capstone\Data\\2019 nCoV wastewater 07222020_results_AlteredForCapstone.xlsx'

data = pd.read_excel(excel_file, sheet_name='Results')

data['Particle_Density'] = "N/A"

# grouped_data = data.groupby(["Sample Name", "Target Name"])

# for name, group in grouped_data:
#     print("Group name: ", name)
#     print('-' * 27)
#     group.loc[group["Sample Name"] == "PTC 1:10", "Particle_Density"] = 20000
#     group.loc[group["Sample Name"] == "PTC 1:100", "Particle_Density"] = 2000
#     group.loc[group["Sample Name"] == "PTC 1:1000", "Particle_Density"] = 200
#     print(group, end="\n\n")

# grouped_data = grouped_data.concat(["Sample Name", "Target Name"])

# print(grouped_data)

selectedData = data.loc[:, ['Sample Name', 'Target Name', 'CT', 'Ct Mean', 'Particle_Density']]

selectedData.loc[selectedData["Sample Name"] == "PTC 1:10", "Particle_Density"] = 20000
selectedData.loc[selectedData["Sample Name"] == "PTC 1:100", "Particle_Density"] = 2000
selectedData.loc[selectedData["Sample Name"] == "PTC 1:1000", "Particle_Density"] = 200

N1plotData = selectedData.loc[selectedData["Target Name"] == "N1", ['Ct Mean', 'Particle_Density']]
N2plotData = selectedData.loc[selectedData["Target Name"] == "N2", ['Ct Mean', 'Particle_Density']]

N1plotData.plot()
plot.show()
N2plotData.plot()
plot.show()

print(selectedData)


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

