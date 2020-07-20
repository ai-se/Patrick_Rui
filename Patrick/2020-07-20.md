# Questions from last submission (ASE2020) & Plans for ICSE/TSE

## Problem A
![meeting720](https://user-images.githubusercontent.com/16036156/87945498-cfd0c380-ca6e-11ea-82b5-480678c75fc3.png)
- Can we do better on predicting about open issue?
### Potential Solution
- Group projects into different categories (clustering), and do predictions on each of groups.
### Progress
- Applied K-MEANS to cluster old projects into groups, with elbow and silhouette suggestions about n_clusters. [Link](https://github.com/ai-se/Patrick_Rui/blob/master/Patrick/2020-06-25.md)
- Grouping methods used by He et al. [Link](https://ieeexplore.ieee.org/abstract/document/6681337)
- Try Autoencoder


## Problem B
![meeting720 (1)](https://user-images.githubusercontent.com/16036156/87946512-1ffc5580-ca70-11ea-8d2a-d400c464e41c.png)
- There may be more useful indicators for better health predictions.
### Potential Solution
- Consult with industrial domain experts for their opinion about key features of success/fail projects.
- Convert those key features into new indicators for further predictions.
### Progress
- Domain expert Kate Stewart has provided a list of key features for project success/failure prodiction. [Link](https://docs.google.com/spreadsheets/d/18LEBbOJNzLoQ_2AqGDmcmzik2qmWatpTnU6ZEgbTOWM/edit#gid=0)
- "Monthly new contributors" has been implemented as a new indicators. [Link](https://github.com/ai-se/Patrick_Rui/blob/master/Patrick/2020-07-06.md)
- Predicting "Monthly new contributors" has got good results in preliminary experiments. [Link](https://docs.google.com/spreadsheets/d/1hQPBHSiP1cB1biBG_dqZU_VjO4IWsonhemOFKrB-nXE/edit#gid=1929673561)
- Another promising new feature "domain diversity" is in progress. [Link](https://docs.google.com/spreadsheets/d/1hQPBHSiP1cB1biBG_dqZU_VjO4IWsonhemOFKrB-nXE/edit#gid=852358286)


## Problem C
![meeting720 (3)](https://user-images.githubusercontent.com/16036156/87949734-6653b380-ca74-11ea-9bce-5162aab7adef.png)
- Do we get enough literature review to find state-of-the-art? What algorithms are commonly explored but not used in our experiments?
### Potential Solution
- Do an updated literature review and apply new methods into our benchmarks.
### Progress
- A list of updated literature review. [Link](https://docs.google.com/spreadsheets/d/1455ltmaXmjG1x-abHVM2jHWi_6K3isZfaYwjK-YSgpQ/edit#gid=0)
- Methods "linear regression with Box-Cox power transform" and "LSTM" are in progress.


## Problem D
![meeting720 (2)](https://user-images.githubusercontent.com/16036156/87948028-2ab7ea00-ca72-11ea-9012-0951155ba217.png)
- Can we simplify and generalize the prediction procedures?
### Potential Solution
- Use only first 10/20/30 months' data as training if it's enough.
- Group projects into different categories and show they can be treated as just a few dozen projects (clustering). Put a new project into its home cluster then use old models to predict this new project.
### Progress
- For sample project "Zephyr", preliminary results show that first 20 month data for training can provide good performance on new contributor pridiction. [Link](https://docs.google.com/spreadsheets/d/1hQPBHSiP1cB1biBG_dqZU_VjO4IWsonhemOFKrB-nXE/edit#gid=1929673561)
- For merged projects and transfered projects, experiment results are in progress. [Link](https://docs.google.com/spreadsheets/d/1O1oZ5j-786hZ-XKWFRX0sMm-P8RwHwKnZmJRXvXe-Kk/edit#gid=159027035)


## Plans for ICSE/TSE
With Problem A-D resolved, it would be a good idea to put those results together for a new paper about more comprehensive project health prediction, with old issue fixed, industrial expert validated, efficiency improved and benchmarked renewed.
