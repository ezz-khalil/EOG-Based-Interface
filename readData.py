from signal import signal
import numpy as np
import os
import csv


class readData:
    def CombineSignal(self, horizontalPath, verticalPath, className, x, outputPath):
        horizontalComponent = np.loadtxt(horizontalPath)
        verticalComponent = np.loadtxt(verticalPath)

        CombinedSignal = np.hstack(
            [horizontalComponent.reshape(-1, 1), verticalComponent.reshape(-1, 1)]
        )

        np.savetxt(f"{outputPath}/{className}{x}.txt", CombinedSignal, fmt="%d %d")

    def CombineData(self, outputPath, datasetsPath):
        classes = ["yukari", "asagi", "sol", "sag", "kirp"]
        if not os.path.exists(outputPath):
            os.mkdir(outputPath)
        for class_name in classes:
            for i in range(1, 21):
                self.CombineSignal(
                    os.path.join(datasetsPath, f"{class_name}{i}h.txt"),
                    os.path.join(datasetsPath, f"{class_name}{i}v.txt"),
                    class_name,
                    i,
                    outputPath,
                )

    def CreateCSV(self, data_csv):
        classes = ["yukari", "asagi", "sol", "sag", "kirp"]
        move = ["Up", "Down", "Left", "Right", "Blink"]
        with open(data_csv, "w", newline="") as file:
            # create a CSV writer object
            writer = csv.writer(file)
            writer.writerow(["signal", "move"])
            for filename in sorted(os.listdir("combined dataset")):
                for classs in classes:
                    if filename.startswith(classs):
                        signal = np.loadtxt(f"combined dataset/{filename}")
                        reversedSignal = signal[::-1]
                        writer.writerow(
                            [
                                signal,
                                move[classes.index(classs)],
                            ]
                        )
                        writer.writerow(
                            [
                                reversedSignal,
                                move[classes.index(classs)],
                            ]
                        )
