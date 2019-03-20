# Blood-Pressure-Mesurement
THIS WAS A PART OF Huawei Honorcup Marathon 1 by Huawei
Estimating systolic (SBP) and diastolic (DBP) blood pressure for a given individual by recorded photoplethysmography (PPG) and electrocardiography (ECG) signals.
Background

Blood pressure is pressure that blood applies to the wall of a particular artery (with respect to atmospheric pressure). Since the flux of blood is pulsating, blood pressure is usually characterized by two values: minimal (diastolic) and maximal (systolic) blood pressure. Under various conditions blood pressure for a given individual may be different. Measuring of blood pressure usually requires a 1 minute procedure during which an artery in the hand is compressed by a cuff. Since the procedure is relatively sophisticated, simpler methods of estimation of blood pressure are potentially of great value.

Photoplethysmography (PPG) is an optical method for detection changes in blood volume in a part of a body (in our case it is a finger). A PPG signal corresponds to the amount of light absorbed by the finger, and thus depends on the amount of blood in the finger. Electrocardiography (ECG) is a method of registering electrical activity of the heart. An ECG signal corresponds to the difference in electrical potential of two electrodes located on the body.

Both ECG and PPG signals implicitly characterize the state of the cardiovascular system of the body. Therefore, it seems reasonable that these signals can be used to estimate blood pressure. However, the problem to predict blood pressure for all population using only the ECG and PPG signals is quite difficult. For this competition, a weaker problem is posed: predict SBP and DBP for each given individual under different conditions provided that several "calibration" records for that individual are known. The calibration records contain the values of SBP and DBP as well as the traces of PPG and ECG signals.

Input
You can download the data by the link https://assets.codeforces.com/files/huawei/blood-pressure-estimation-data.zip.

The data files are split across 3 folders: data_train, data_test1_blank, and data_test2_blank. Each file name has the following form:

subjXXlogYYYY.csv
where XX is the identity number of a person and YYYY is the record number. Each file has the following contents:

SBP,DBP
PPG_1,ECG_1
PPG_2,ECG_2
PPG_3,ECG_3
....,....
where the first row contains the values of SBP and DBP, and the subsequent rows contain the samples of the PPG and ECG signals. The sampling rate is 500 Hz.

Please note that parts of some ECG and PPG signal traces may be corrupted. For instance, it can happen that the ECG electrodes are applied only after the start of recording. This leads to the initial part of the ECG signal trace being absolutely not valid. Another problem that sometimes happen is saturation of PPG signal. Be careful to preprocess the broken traces first.

The files located in data_train folder are intended for training. All such files contain the ground truth SBP a DBP values.
