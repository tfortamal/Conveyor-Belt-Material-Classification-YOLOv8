### ⚠️ This is just a demonstration of YOLOv8 implementation to solve real-life problems. The data set is for private use only. However, all the source code is available. In my example the name of the conveyor belt J1C1 

# J1C1 Material Dataset Description:


class_name    | class_id      | number_of_images                |
 ------------ | ------------- | ------------                    | 
| dolomite_limestone_j1c1     | 0         |        10000        |
| empty_j1c1                  | 1         |        10000        |
| half_filled_j1c1            | 2         |        10000        |
| iron_ore_fines_j1c1         | 3         |        10000        |
| pallet_j1c1                 | 4         |        10000        |
| total                       |           |        50000        |


## **Data Structure for Detection:**
```bash
DetectionData______
                  |
                  |____train________
                  |                 |_____dolomite_limestone_j1c1____
                  |                 |                                |___image
                  |                 |                                |
                  |                 |                                |___label
                  |                 |_____empty_j1c1_________________
                  |                 |                                |___image
                  |                 |                                |
                  |                 |                                |___label
                  |                 |_____half_filled_j1c1___________
                  |                 |                                |___image
                  |                 |                                |
                  |                 |                                |___label
                  |                 |_____iron_ore_fines_j1c1________
                  |                 |                                |___image
                  |                 |                                |
                  |                 |                                |___label
                  |                 |_____pallet_j1c1________________
                  |                                                  |___image
                  |                                                  |
                  |                                                  |___label
                  |____test_________
                  |                 |_____dolomite_limestone_j1c1__[Contains image and label]
                  |                 |
                  |                 |_____empty_j1c1____[Contains image and label]
                  |                 |
                  |                 |_____half_filled_j1c1___[Contains image and label]
                  |                 |
                  |                 |_____iron_ore_fines_j1c1___[Contains image and label]
                  |                 |
                  |                 |_____pallet_j1c1___[Contains image and label]
                  |
                  |____val__________
                                    |_____dolomite_limestone_j1c1___[Contains image and label]
                                    |
                                    |_____empty_j1c1___[Contains image and label]
                                    |
                                    |_____half_filled_j1c1___[Contains image and label]
                                    |
                                    |_____iron_ore_fines_j1c1___[Contains image and label]
                                    |
                                    |_____pallet_j1c1___[Contains image and label]
```

### lable format:
lable for 1.jpg --> 1.txt
contents of 1.txt --> [the lable file contains class id and 4 points]
> class_id x1 y1 x2 y2 x3 y3 x4 y4
> 2 250 79 390 676 1077 667 474 44 (not normalized for YOLO models)
> 1 0.5385044642857144 0.5376984126984128 0.6640625000000001 0.8725198412698415 (for YOLO models)

## Data Structure for Classification:
```bash

ClassificationData______
                        |
                        |____train________
                        |                 |_____dolomite_limestone_j1c1___[Contains image only]
                        |                 |                    
                        |                 |_____empty_j1c1___[Contains image only]
                        |                 |                    
                        |                 |_____half_filled_j1c1___[Contains image only]
                        |                 |                    
                        |                 |_____iron_ore_fines___[Contains image only]
                        |                 |                    
                        |                 |_____pallet_j1c1___[Contains image only]            
                        |____test_________
                        |                 |_____dolomite_limestone_j1c1___[Contains image only]
                        |                 |
                        |                 |_____empty_j1c1___[Contains image only]
                        |                 |
                        |                 |_____half_filled_j1c1___[Contains image only]
                        |                 |
                        |                 |_____iron_ore_fines___[Contains image only]
                        |                 |
                        |                 |_____pallet_j1c1___[Contains image only]
                        |
                        |____val__________
                                          |_____dolomite_limestone_j1c1___[Contains image only]
                                          |
                                          |_____empty_j1c1___[Contains image only]
                                          |
                                          |_____half_filled_j1c1___[Contains image only]
                                          |
                                          |_____iron_ore_fines___[Contains image only]
                                          |
                                          |_____pallet_j1c1___[Contains image only]

```

---
## License 
### Author: _**Tamal Das** August, 2023 for **[Divsoft Solutions](https://divsoftsolutions.com)**_
