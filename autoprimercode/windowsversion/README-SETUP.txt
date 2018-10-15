Autoprimer V. 1.0

Introduction:

Autoprimer is a wrapper program that combines two existing programs (Primer3 and Primer Pooler) as well as its own implementation of Blast functionality to enable an easy, user friendly and automated workflow for picking and designing primers. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~INSTALLATION INSTRUCTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Some configuration is necessary everytime the program is put on a new machine. In general, if the new machines system has the same OS as another, then the included files should work out of the box. If it does not, please refer to the instructions below.


2. Check what build of Windows you have. This can be done by running the 'dxdiag' command. 

	- press the Windows start menut button on the bottom left, type in dxdiag into the entry box and press enter. Diagnostic information should come up and it should tell you whether you are running 32 or 64 bit Windows.


3. Depending on what version of Windows you possess, you will need to download either the 32 or 64 bit version of Primer Pooler. (You may skip this step if the Pooler is working.)

	- download site: http://people.ds.cam.ac.uk/ssb22/pooler/
	
	- drag the pooler.exe to the same folder as the autoprimer executable, then rename the 'pooler' file to 'pooler64'


4. Download and install a GNU compiler that allows you to compile C programs on Windows. (If you already have the primer3 program installed and working, skip this step.)

	- If you already have 'make' functionality on your machine, you can skip to the line after the next.

	- Install this package (TDM-GCC): http://tdm-gcc.tdragon.net/download (choose the one appropriate for your Windows version)

	- Open up a command prompt: go to your windows menu and type in 'cmd' and press enter, a command prompt should appear

	- Check the filepath of your primer3-2.x.x folder (depends on your version, currently the latest release it works with is 2.3.7) 

	- For example, if your primer 3 filepath is like so: C:\Users\mqian\Desktop\CGIProject\primerversions\primer3-2.3.7\src\ then type 'cd' followed by a space then drag the src folder into the command prompt. 

	- The text should in the command prompt should now look like 'cd C:\Users\mqian\Desktop\CGIProject\primerversions\primer3-2.3.7\src\' press enter and you will now be in the 'src' folder in the command prompt

	- Type 'mingw32-make' into the command prompt and press enter. Let the compiler finish running. When it is completed, there should be an executable file called 'primer3_core'. That is the launcher for the primer3 program.


5. After having a working version of primer3 on your computer, go ahead and edit the primer3corelocation.txt file and copy and paste in the filepath of your new primer3_core.exe. 

	- As an example, my primer3_core.exe is located at 'C:\Users\mqian\Desktop\CGIProject\primerversions\primer3-2.3.7\src\primer3_core.exe'

	- I will copy and paste that over whatever is in the primer3corelocation file and add an extra backslash ('\') to the beginning so it looks like C:\\ instead of C:\.


6. When using thermodynamic properties in primer3, it is necessary to edit the filepath where the thermodynamic parameter files are held as it changes based on each machine. 

	- Open up any potential input file (you could do this just once and keep it as a template) and find the line 'PRIMER_THERMODYNAMIC_PARAMETER_PATH=' and replace what follows the = sign with the filepath of the thermodynamic files

	- They will be located in the primer3_config folder in the src folder. As an example, the final line in the input file should be: 'PRIMER_THERMODYNAMIC_PARAMETER_PATH=C:\Users\mqian\Desktop\CGIProject\primerversions\primer3-2.3.7\src\primer3_config\'


7. Setup should now be complete. 