# CE-UY 3013 Computing In Civil Engineering Final Project
# Short Reinforced Concrete Column Design Program

This program designs short reinforced concrete columns with an eccentric load acting on it. The initial dimensions of the column and the reinforcing steel bars and lateral reinforcement are initially unknown. The concrete in the columns have a compression strength of 4 ksi and the steel reinforcement has a yielding strength of 60 ksi in order to utilize the design tables and figures provided in the "Design Tables" folder.

Assumptions:
* This code assumes the user wants to design a short concrete reinforced
* These columns DO NOT fail due to buckling
* The user wants to design a SQUARE column with reinforcing on all 4 sides
* This user wants to design CIRCULAR columns
* All columns are reinforced with steel bars
* This program assumes that the compressive strength of concrete is 4 ksi
* This program assumes that the yielding strength of the rebars is 60 ksi
* The ratio of steel reinforcement can only be between 0.01 and 0.08, inclusive
* If the ratio is not known, the steel reinforcement ratio is taken to be 0.01
  to produce a conservative design
* This program assumes a concrete cover of 3 inches to comply with ACI code
* This program also assumes compression controlled columns are being produced

Inputs:
* The desired shape of the column
* Axial loads and moments acting on the column
* The ratio of steel reinforcement area to the cross sectional area of the columns
* The type of lateral reinforcement in the column
* Column dimension and area values read from Table A-14
* Value for rho read from the appropriate Figure number.
* Reinforcing bar number read from Table A-2
* Amount of reinforcing bars read from Table A-2
* Inner core area read from Table A-14
* Size of the bars used in the lateral reinforcement

Outputs:
* The shape of the column
* The dimension of the column
* The dimension of the inner core of the column
* The size of the lateral reinforcement
* The spacing between the lateral reinforcement
* The amount of reinforcing bars in the column
* The size of the reinforcing bars in the column

## Setup

To use the program, you can download this repository and use it in your preferred virtual environment.

## Example of how to use the Program
## *SQUARE COLUMN EXAMPLE*

This part of the code is all the initial inputs

```
#Initial axial load is 890 kips
#Initial moment load is 390 kip-feet
#Using tied reinforcing

#This is the assumption made for concrete and steel
#Concrete has a compressive strength of 4 ksi
#Steel yields at 60 ksi


f_conc = 4
f_yield = 60


#This is to determine the shape of the column that will be designed
col_type = str(input("Type 'square' or 'circular' to determine the shape of the column design: "))

while col_type != 'square' and col_type != 'circular':
    col_type = str(input('Retype square or circular to determine the shape of the column design: '))


#This is to determine the forces and moments that will act on the column
p_fact = float(input('Input factored axial load in Kips: '))
m_fact = float(input('Input factored moment load in Kip-ft: '))

#This is to determine the if the ratio of steel reinforcement is known.
#This value is required to determine the gross area of the column
display("Type 'yes' or 'no'")
ratio_g = input('Is the ratio of steel reinforcement to cross sectional area known? :')

#If the ratio is not known, it is assumed to be 0.01
while ratio_g != 'yes' and ratio_g != 'no':
  display("'Type 'yes' or 'no'")
  ratio_g = input('Is the ratio of steel reinforcement to cross sectional area known? :')

if ratio_g == 'yes':
  rho_g = float(input('Input ratio of reinforcement area to cross-sectional area of column: '))
elif ratio_g == 'no':
  rho_g = 0.01

#This is to determine the spiral type that will be used for the column.
#Square columns usually have ties to prevent the reinforcing from coming out of the column.
#Circular columns usually have spirals to prevent the reinforcing from coming out of the column.
spiral_type = input("Type 'tied' or 'spiral' for type of tie reinforcing: '")

while spiral_type != 'tied' and spiral_type != 'spiral':
  spiral_type = input("'Retype 'tied' or 'spiral' for type of tie reinforcing: '")

#The phi values for either case are due to the assumption that the columns are compression controlled
#The phi values are used to determine the gross area of the column
if spiral_type == 'tied':

    phi = 0.65

    gross_area = p_fact / (0.8 * phi * (0.85 * f_conc * (1 - rho_g) + (f_yield * rho_g)))

elif spiral_type == 'spiral':

    phi = 0.75

    gross_area = p_fact / (0.85 * phi * (0.85 * f_conc * (1 - rho_g) + (f_yield * rho_g)))

#The code displays the calculated gross area of the column and the calculated core size
gross_area = round(gross_area, 0)
display('The gross area of the core is: {} square inches'.format(gross_area))

core_size = (gross_area)**0.5
core_size = round(core_size, 1)
display('The size of the column is {} inches'.format(core_size))
```

The code up to this portion displays the following after entering all the inputs

```
Type 'square' or 'circular' to determine the shape of the column design: square
Input factored axial load in Kips: 890
Input factored moment load in Kip-ft: 390
Type 'yes' or 'no'
Is the ratio of steel reinforcement to cross sectional area known? :no
Type 'tied' or 'spiral' for type of tie reinforcing: 'tied
The gross area of the core is: 432.0 square inches
The size of the column is 20.8 inches
```
The following portion requires the user to read values from Table A-14.
Table A-14 can be found in the 'Design Tables' folder.
The values read from Table A-14 are:
* 22 for the core size of the column
* 484 inches square for the area of the columns

The above values are used for the next block of code.

```
#The next two inputs are supposed to be larger than the calculated gross area and core size
selected_column_size = int(input('Input core size from Table A-14: '))

selected_column_area = float(input('Input area size from Table A-14: '))

#This calculation assumes a 3 inch covering around the steel bars. This is to comply with ACI code.
#This also assumes #3 bars for the tie reinforcement
#This also assumes #8 bars for the column reinforcement
inner_core = selected_column_size - 2 * 1.5 - 2 * (3/8) - (8/8)

#This is to obtain a value that will help determine which design figure to use.
gamma = round(inner_core / selected_column_size , 1)

req_k = round(p_fact / (phi * f_conc * selected_column_area) , 2)

req_r = round(m_fact * 12 / (phi * f_conc * selected_column_area * selected_column_size) , 2)

#Displays the Y and X-axis values to use for the design figure.
display('Enter table with K value: ', req_k)
display('Enter table with R value: ', req_r)

#These next conditional statements determine which figure will be used with the calculated K and R values
if gamma == 0.7:

  if col_type == 'square':
    display('Use Figure A-17')

  elif col_type == 'circular':
    display('Use Figure A-20')

elif gamma == 0.8:

  if col_type == 'square':
    display('Use Figure A-18')

  elif col_type == 'circular':
    display('Use Figure A-21')

elif gamma == 0.9:

  if col_type == 'square':
    display('Use Figure A-19')

  elif col_type == 'circular':
    display('Use Figure A-22')
```

The program will display the following after inputting the values from Table A-14.
The last line is important because it determines which Figure will be used to read an important value for the design.

```
Input core size from Table A-14: 22
Input area size from Table A-14: 484
Enter table with K value:
0.71
Enter table with R value:
0.17
Use Figure A-18
```

Figure A-18 is used in this case. Figure A-18 can be found in the Design Tables
folder. The value that is supposed to be read is the rho t value. It ranges
between 0.01 and 0.08. The value read from the figure is a value that is in between
that range of values. The value that is read from the figure must fall between
the blue lines and must have a Kmax above 1.0 to be considered compression
controlled. In this example, I read a value of 0.028 for the rho value.

```
#The Y-axis is the req_k value. The interval for the Y-axis is 0.04.
#The X-axis is the req_r value. The interval for the X-axis is 0.01.
rho = float(input('Input rho value from the figure given above: '))

#Determines the required area for the steel reinforcement
area_steel = rho * selected_column_area

display(round(area_steel,2))
```
The following is displayed after this selection of rho. The last line in the following block is the required area of steel. The user must select an area of
steel larger than 13.55 from Table A-2.

```
Input rho value from the figure given above: 0.028
13.55
```

The next portion of the code requires the use of Table A-2. Table A-2 can be found
within the Design Tables folder. The size of the bar that I used for this example
was a #9 bar. I read this value off of the top of Table A-2.

The next value I read was the number of bars which is the column on the left side of Table A-2. I decided to select 14 bars to have an area of 14 inches square. However, due to the assumption of square columns being reinforced on all four sides, the program prompted me to select an amount of bars that is a multiple of four. I selected 16 bars.

Then the code displays the inner core size: 19.
I had to check on Table A-14 if 16 bars can fit in an inner core of 19 inches.
To do this, go to Table A-14 and find 19 in the core size column.
Follow along its row and since I am designing a square column, I check on the right
side of Table A-14. I find the column for Bar number #9 and check the number.
The number at the intersection is 16. This number is the max number of bars that can fit in the column.

If the bars do not fit in the core, the program will prompt the user to resize their reinforcement bars by selecting different bar size and number from Table A-2.
The user must still select a combination that results in a steel area larger than the 13.55 that was displayed above. If the user cannot find a combination that works after 5 attempts, the program will end which forces the user to start the program over from the beginning. This will allow the user to go through the program again and select a larger core size and area from Table A-2.

The last input is the size of the reinforcing bars. Generally #3 bars are used for lateral reinforcement, but sizes 4 and 5 can be used too.

```
#Required to determine if the bars fit in the column.
#This determines the size number of the bar.
#Size of bars that are used in Table A-14 are between 2 and 11.
bar_size = int(input('Type bar number from Table A-2: '))

#Required to determine if the bars fit in the column.
#This determines the amount of bars in the column.
if col_type == 'square':
  display('Number of bars has to be a multiple of 4 for even distribution of force in column.')
  number_of_bars = int(input('Select number of bars from Table A-2: '))

  while number_of_bars%4 != 0:
    display('Number of bars has to be a multiple of 4.')
    number_of_bars = int(input('Reselect number of bars from Table A-2: '))

else:

  number_of_bars = int(input('Type number of bars from Table A-2: '))

#This is to determine if the bars can fit in the inner core.
#This inner core size is to determine the core of the column after making an initial selection of the column.
#If the reinforcing does not fit in this smaller area, the column will not work.
#A different bar size and amount of bars must be selected in order to fit in the column
inner_core_size = selected_column_size - 3

display('Core size: ', inner_core_size)
display('Check on Table A-14. Do {} bars fit in the displayed core size area?'.format(number_of_bars))

bar_check = input("Type 'yes' or 'no': ")

count = 0

#This gives the user 5 more attempts to resize their bars before they have to resize the column
#If the user must resize their column, they must select larger values from Table-14
#If they cannot find an adequate size and amount of bars to fit in the column,
#the program will stop working. This is to allow for the user to resize their column.
while bar_check == 'no' and count <= 4:

  count = count + 1

  display('You must reselect a bar size and amount of bars ')

  bar_size = int(input('Reinput bar number: '))

  number_of_bars = int(input('Reinput number of bars: '))

  display('Do {} bars fit in the displayed core size?'.format(number_of_bars))

  bar_check = input("Type 'yes' or 'no': ")


#This kills the program.
#The user has to restart the program from the beginning in order to resize their column.
if count == 5:

  if bar_check == 'no':

    display('You must resize the column core and try again')
    exit()

#Number 3, 4, and 5 bars are used for ties and spiral reinforcement
size_ties = int(input("Input '3', '4', or '5' for size of ties: "))

#The smallest value of the following three checks is used to determine the spacing of the reinforcing ties
#These checks are from the ACI code
if col_type == 'square':

  spacing_one = 16 * (bar_size/8)
  spacing_two = 48 * (size_ties/8)
  spacing_three = selected_column_size

  spacing_ties = min(spacing_one, spacing_two, spacing_three)

#spiral reinforcement are determined differently from ties
elif col_type == 'circular':

  #To determine the spacing of ties, the area of the inner core is required
  #This displays the size of the inner core
  display('From Table A-14, input the area of the {} in core.'.format(inner_core_size))

  #This is the area of the inner core from design Table A-14
  inner_core_area = float(input('Input inner core area from Table A-14: '))

  #Determines the required ratio for the spacing of the spiral
  required_rho = 0.45*((selected_column_area / inner_core_area ) - 1 ) * ( f_conc / f_yield )

  spacing_ties = (4 * ((3.1415 * (size_ties/8)**2) / 4)) / (inner_core_size * required_rho)

  #Rounds the spiral spacing to the nearest quarter inch
  spacing_ties = round(spacing_ties*4)/4
```

The following is displayed after going through the previous block of code and inputting all the values.
```
Type bar number from Table A-2: 9
Number of bars has to be a multiple of 4 for even distribution of force in column.
Select number of bars from Table A-2: 14
Number of bars has to be a multiple of 4.
Reselect number of bars from Table A-2: 16
Core size:
19
Check on Table A-14. Do 16 bars fit in the displayed core size area?
Type 'yes' or 'no': yes
Input '3', '4', or '5' for size of ties: 3
```

This last block of code displays the shape of the column, all the dimensions of the column, lateral reinforcement, and reinforcement bars.

```
#This last block of code displays all the necessary information required to design the column.
#The first value displayed is the shape of the column

#The second value displayed is the dimension of the column
#This is the length of the sides of a square column
#or the diameter of a circular column.

#The third value displayed is the size of the inner core of the column
#A square column contains a square inner core.
#A circular column contains a circular inner core.

#The fourth value displayed is the size of the reinforcing ties or spirals
#The fifth value displayed is the spacing of these ties or spirals

#The sixth value shown is the amount of reinforcing bars.
#This is the QUANTITY of the bars.

#The last value displayed is the SIZE of the rebars

display('The shape of the column is: {}'.format(col_type),
        'The selected column size is: {} inches.'.format(selected_column_size),
        'The inner core size is: {} inches.'.format(inner_core),
        'The ties are #{} ties'.format(size_ties),
        'with {} inch spacing on center.'.format(spacing_ties),
        'The column contains {}'.format(number_of_bars),
        'size #{} bars.'.format(bar_size)
        )
```

The program will display the following:

```
The shape of the column is: square
The selected column size is: 22 inches.
The inner core size is: 17.25 inches.
The ties are #3 ties
with 18.0 inch spacing on center.
The column contains 16
size #9 bars.
```

This is the end of the square column example.

## Example of how to use the Program
## *CIRCULAR COLUMN EXAMPLE*

This part of the code is all the initial inputs

```
#Initial axial load is 890 kips
#Initial moment load is 390 kip-feet
#Using tied reinforcing

#This is the assumption made for concrete and steel
#Concrete has a compressive strength of 4 ksi
#Steel yields at 60 ksi


f_conc = 4
f_yield = 60


#This is to determine the shape of the column that will be designed
col_type = str(input("Type 'square' or 'circular' to determine the shape of the column design: "))

while col_type != 'square' and col_type != 'circular':
    col_type = str(input('Retype square or circular to determine the shape of the column design: '))


#This is to determine the forces and moments that will act on the column
p_fact = float(input('Input factored axial load in Kips: '))
m_fact = float(input('Input factored moment load in Kip-ft: '))

#This is to determine the if the ratio of steel reinforcement is known.
#This value is required to determine the gross area of the column
display("Type 'yes' or 'no'")
ratio_g = input('Is the ratio of steel reinforcement to cross sectional area known? :')

#If the ratio is not known, it is assumed to be 0.01
while ratio_g != 'yes' and ratio_g != 'no':
  display("'Type 'yes' or 'no'")
  ratio_g = input('Is the ratio of steel reinforcement to cross sectional area known? :')

if ratio_g == 'yes':
  rho_g = float(input('Input ratio of reinforcement area to cross-sectional area of column: '))
elif ratio_g == 'no':
  rho_g = 0.01

#This is to determine the spiral type that will be used for the column.
#Square columns usually have ties to prevent the reinforcing from coming out of the column.
#Circular columns usually have spirals to prevent the reinforcing from coming out of the column.
spiral_type = input("Type 'tied' or 'spiral' for type of tie reinforcing: '")

while spiral_type != 'tied' and spiral_type != 'spiral':
  spiral_type = input("'Retype 'tied' or 'spiral' for type of tie reinforcing: '")

#The phi values for either case are due to the assumption that the columns are compression controlled
#The phi values are used to determine the gross area of the column
if spiral_type == 'tied':

    phi = 0.65

    gross_area = p_fact / (0.8 * phi * (0.85 * f_conc * (1 - rho_g) + (f_yield * rho_g)))

elif spiral_type == 'spiral':

    phi = 0.75

    gross_area = p_fact / (0.85 * phi * (0.85 * f_conc * (1 - rho_g) + (f_yield * rho_g)))

#The code displays the calculated gross area of the column and the calculated core size
gross_area = round(gross_area, 0)
display('The gross area of the core is: {} square inches'.format(gross_area))

core_size = (gross_area)**0.5
core_size = round(core_size, 1)
display('The size of the column is {} inches'.format(core_size))
```

The code up to this portion displays the following after entering all the inputs

```
Type 'square' or 'circular' to determine the shape of the column design: circular
Input factored axial load in Kips: 890
Input factored moment load in Kip-ft: 390
Type 'yes' or 'no'
Is the ratio of steel reinforcement to cross sectional area known? :no
Type 'tied' or 'spiral' for type of tie reinforcing: 'spiral
The gross area of the core is: 352.0 square inches
The size of the column is 18.8 inches
```
The following portion requires the user to read values from Table A-14.
Table A-14 can be found in the 'Design Tables' folder.
The values read from Table A-14 are:
* 23 for the core size of the column
* 415.5 inches square for the area of the columns

The above values are used for the next block of code.

```
#The next two inputs are supposed to be larger than the calculated gross area and core size
selected_column_size = int(input('Input core size from Table A-14: '))

selected_column_area = float(input('Input area size from Table A-14: '))

#This calculation assumes a 3 inch covering around the steel bars. This is to comply with ACI code.
#This also assumes #3 bars for the tie reinforcement
#This also assumes #8 bars for the column reinforcement
inner_core = selected_column_size - 2 * 1.5 - 2 * (3/8) - (8/8)

#This is to obtain a value that will help determine which design figure to use.
gamma = round(inner_core / selected_column_size , 1)

req_k = round(p_fact / (phi * f_conc * selected_column_area) , 2)

req_r = round(m_fact * 12 / (phi * f_conc * selected_column_area * selected_column_size) , 2)

#Displays the Y and X-axis values to use for the design figure.
display('Enter table with K value: ', req_k)
display('Enter table with R value: ', req_r)

#These next conditional statements determine which figure will be used with the calculated K and R values
if gamma == 0.7:

  if col_type == 'square':
    display('Use Figure A-17')

  elif col_type == 'circular':
    display('Use Figure A-20')

elif gamma == 0.8:

  if col_type == 'square':
    display('Use Figure A-18')

  elif col_type == 'circular':
    display('Use Figure A-21')

elif gamma == 0.9:

  if col_type == 'square':
    display('Use Figure A-19')

  elif col_type == 'circular':
    display('Use Figure A-22')
```

The program will display the following after inputting the values from Table A-14.
The last line is important because it determines which Figure will be used to read an important value for the design.

```
Input core size from Table A-14: 23
Input area size from Table A-14: 415.5
Enter table with K value:
0.71
Enter table with R value:
0.16
Use Figure A-21
```

Figure A-21 is used in this case. Figure A-21 can be found in the Design Tables
folder. The value that is supposed to be read is the rho t value. It ranges
between 0.01 and 0.08. The value read from the figure is a value that is in between
that range of values. The value that is read from the figure must fall between
the blue lines and must have a Kmax above 1.0 to be considered compression
controlled. In this example, I read a value of 0.034 for the rho value.

```
#The Y-axis is the req_k value. The interval for the Y-axis is 0.04.
#The X-axis is the req_r value. The interval for the X-axis is 0.01.
rho = float(input('Input rho value from the figure given above: '))

#Determines the required area for the steel reinforcement
area_steel = rho * selected_column_area

display(round(area_steel,2))
```
The following is displayed after this selection of rho. The last line in the following block is the required area of steel. The user must select an area of
steel larger than 14.13 from Table A-2.

```
Input rho value from the figure given above: 0.034
14.13
```

The next portion of the code requires the use of Table A-2. Table A-2 can be found
within the Design Tables folder. The size of the bar that I used for this example
was a #10 bar. I read this value off of the top of Table A-2.

The next value I read was the number of bars which is the column on the left side of Table A-2. I decided to select 12 bars.

Then the code displays the inner core size: 20.
I had to check on Table A-14 if 12 bars can fit in an inner core of 20 inches.
To do this, go to Table A-14 and find 20 in the core size column.
Follow along its row and since I am designing a circular column, I check on the left
side of Table A-14. I find the column for Bar number #10 and check the number.
The number at the intersection is 12. This number is the max number of bars that can fit in the column.

If the bars do not fit in the core, the program will prompt the user to resize their reinforcement bars by selecting different bar size and number from Table A-2.
The user must still select a combination that results in a steel area larger than the 14.13 that was displayed above. If the user cannot find a combination that works after 5 attempts, the program will end which forces the user to start the program over from the beginning. This will allow the user to go through the program again and select a larger core size and area from Table A-2.

The last input is the size of the reinforcing bars. Generally #3 bars are used for lateral reinforcement, but sizes 4 and 5 can be used too. This example uses size 3 lateral reinforcing bars.

```
#Required to determine if the bars fit in the column.
#This determines the size number of the bar.
#Size of bars that are used in Table A-14 are between 2 and 11.
bar_size = int(input('Type bar number from Table A-2: '))

#Required to determine if the bars fit in the column.
#This determines the amount of bars in the column.
if col_type == 'square':
  display('Number of bars has to be a multiple of 4 for even distribution of force in column.')
  number_of_bars = int(input('Select number of bars from Table A-2: '))

  while number_of_bars%4 != 0:
    display('Number of bars has to be a multiple of 4.')
    number_of_bars = int(input('Reselect number of bars from Table A-2: '))

else:

  number_of_bars = int(input('Type number of bars from Table A-2: '))

#This is to determine if the bars can fit in the inner core.
#This inner core size is to determine the core of the column after making an initial selection of the column.
#If the reinforcing does not fit in this smaller area, the column will not work.
#A different bar size and amount of bars must be selected in order to fit in the column
inner_core_size = selected_column_size - 3

display('Core size: ', inner_core_size)
display('Check on Table A-14. Do {} bars fit in the displayed core size area?'.format(number_of_bars))

bar_check = input("Type 'yes' or 'no': ")

count = 0

#This gives the user 5 more attempts to resize their bars before they have to resize the column
#If the user must resize their column, they must select larger values from Table-14
#If they cannot find an adequate size and amount of bars to fit in the column,
#the program will stop working. This is to allow for the user to resize their column.
while bar_check == 'no' and count <= 4:

  count = count + 1

  display('You must reselect a bar size and amount of bars ')

  bar_size = int(input('Reinput bar number: '))

  number_of_bars = int(input('Reinput number of bars: '))

  display('Do {} bars fit in the displayed core size?'.format(number_of_bars))

  bar_check = input("Type 'yes' or 'no': ")


#This kills the program.
#The user has to restart the program from the beginning in order to resize their column.
if count == 5:

  if bar_check == 'no':

    display('You must resize the column core and try again')
    exit()

#Number 3, 4, and 5 bars are used for ties and spiral reinforcement
size_ties = int(input("Input '3', '4', or '5' for size of ties: "))

#The smallest value of the following three checks is used to determine the spacing of the reinforcing ties
#These checks are from the ACI code
if col_type == 'square':

  spacing_one = 16 * (bar_size/8)
  spacing_two = 48 * (size_ties/8)
  spacing_three = selected_column_size

  spacing_ties = min(spacing_one, spacing_two, spacing_three)

#spiral reinforcement are determined differently from ties
elif col_type == 'circular':

  #To determine the spacing of ties, the area of the inner core is required
  #This displays the size of the inner core
  display('From Table A-14, input the area of the {} in core.'.format(inner_core_size))

  #This is the area of the inner core from design Table A-14
  inner_core_area = float(input('Input inner core area from Table A-14: '))

  #Determines the required ratio for the spacing of the spiral
  required_rho = 0.45*((selected_column_area / inner_core_area ) - 1 ) * ( f_conc / f_yield )

  spacing_ties = (4 * ((3.1415 * (size_ties/8)**2) / 4)) / (inner_core_size * required_rho)

  #Rounds the spiral spacing to the nearest quarter inch
  spacing_ties = round(spacing_ties*4)/4
```

The following is displayed after going through the previous block of code and inputting all the values.

```
Type bar number from Table A-2: 10
Type number of bars from Table A-2: 12
Core size:
20
Check on Table A-14. Do 12 bars fit in the displayed core size area?
Type 'yes' or 'no': yes
Input '3', '4', or '5' for size of ties: 3
From Table A-14, input the area of the 20 in core.
Input inner core area from Table A-14: 314.2
```

This last block of code displays the shape of the column, all the dimensions of the column, lateral reinforcement, and reinforcement bars.

```
#This last block of code displays all the necessary information required to design the column.
#The first value displayed is the shape of the column

#The second value displayed is the dimension of the column
#This is the length of the sides of a square column
#or the diameter of a circular column.

#The third value displayed is the size of the inner core of the column
#A square column contains a square inner core.
#A circular column contains a circular inner core.

#The fourth value displayed is the size of the reinforcing ties or spirals
#The fifth value displayed is the spacing of these ties or spirals

#The sixth value shown is the amount of reinforcing bars.
#This is the QUANTITY of the bars.

#The last value displayed is the SIZE of the rebars

display('The shape of the column is: {}'.format(col_type),
        'The selected column size is: {} inches.'.format(selected_column_size),
        'The inner core size is: {} inches.'.format(inner_core),
        'The ties are #{} ties'.format(size_ties),
        'with {} inch spacing on center.'.format(spacing_ties),
        'The column contains {}'.format(number_of_bars),
        'size #{} bars.'.format(bar_size)
        )
```

The program will display the following:

```
The shape of the column is: circular
The selected column size is: 23 inches.
The inner core size is: 18.25 inches.
The ties are #3 ties
with 2.25 inch spacing on center.
The column contains 12
size #10 bars.
```

This is the end of the circular column example.
