# Stellaris-map-editor 群星地图修改器
改派小软件，可以用来将地图中指定的两个星系位置互换，减少刷极品图的时间。

免责声明：
如果使用此程序，即认可开发者不会对任何使用过程中的问题负责。
禁止任何使用此程序获利的行为。

使用方式：
使用时，请先找到你的存档文件，将其后缀更改为zip并对文件解压。将获取的gamestate文件与此软件放置于同一目录下。
运行此软件，输入你想要调换位置的两个星系的id并回车，当finish出现时，调换完成。
然后将gamestate文件与meta文件重新压缩回.zip文件内，将其后缀修改为.sav获取修改后的存档文件。
你可以通过群星内控制台observe模式观看全地图，并通过debugtooltip查看指定星系的id。
如果你是铁人存档，你可以打开gamestate文件和meta文件，将其中ironman=yes修改为ironman=no（两个文件各一处）来获取一份可以打开控制台的存档。请注意保留原铁人存档的gamestate和meta文件用来修改，这样你才能正常获取成就。

建议：
请务必做好存档备份！推荐仅在开局时使用此程序，本人没有测试游戏中途修改是否会出现bug。
推荐不要调换自己国家视野范围内的星系，不然更改后的地图会比较怪。
如果需要调换的星系包含某个国家，请将其国家全部领土一并调换至新位置并保证其领土依旧相连。否者不确定是否会有bug。
如果需要调换在星云内的星系，你需要进入gamestate文件，找到星云的部分，手动将galactic_object的数值从原本星系id更改会调换的星系id（具体参照群星wiki的改派教程）。
暂时只完美支持椭圆星系开局的地图，如果是悬臂星系开局，请手动对调星系详细信息下对应两个星系的“arm=“数值（具体参照群星wiki的改派教程）。

建议的最后两条未来也许会更新入程序？（也许不会）
祝玩的开心




Small function to swap two systems' locations inside the Stellaris map

Disclaimer:
If you use this software, you agree that the developer will not be responsible for any problem during use.
Any action that seeks profit with this software is prohibited.

Guidance:
First, find your save file(.sav). Change its suffix to .zip and unzip it. Put the gamestate file to the same folder with this software.
Run this software and input the IDs of the two systems that you want to swap. When "finish" appears, you can put the new gamestate file and meta file back into the .zip file and zip them again. Change the suffix back to ".sav".
You can find the IDs of the systems with the observe mode and debugtooltip function during the game.
If you play under ironman, you can first open gamestate and meta files, and change ironman=yes to ironman=no in both files. Then you can do the previous steps to get a save file that can use the control console.

Suggestions:
Make sure you back up before applying any changes!

Hope you enjoy your game!







2024/5/19更新
添加了一个小软件"ironman.py"，现在只需要把ironman.sav文件放置到相同文件夹，运行这个程序，就可以自动更改它的铁人状态啦（从铁人到非铁人，或者从非铁人到铁人）。开局的非铁人档应该是没有办法通过这个软件转换为铁人档的，不过还没有测试过，如果有人能帮忙测试一下就好了。

2024/5/19 Update
A new software "ironman.py" is added. You can directly put ironman.sav file to the same folder with this software to transfer it from ironman to unironmaned or from unironmaned to ironman. It should not be able to transfer an originally unironmaned generated save file to ironman save file to get achievements.
