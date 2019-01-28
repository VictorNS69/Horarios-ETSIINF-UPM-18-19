# Data format
This is the way you have to write the data into the [data.dat](./data.dat)

Each subject must be written in a single line following this format:
```txt
CODE@NAME@TYPE@ECTS@SEMESTER@SCHEDULE
```
- _CODE_ must be a numeric value
- The _NAME_ has to be written in ASCII (without accents or symbols)
- The _TYPE_ must be:
  - BASICA
  - OBLIGATORIA
  - OPCIONAL
 - _ECTS_ must be a numeric value greater than 0 
 - _SEMESTER_ must be a number between 1 and 9 (both inclusive)
 - _SCHEDULE_ must follow the example below
 ```txt
 COURSE_1:OPTION_1,OPTION_2, ... @COURSE_2:OPTION_1 ...
 ```
Example with 2 subjects:
```txt
105000002@LOGICA@Basica@6@1@1M:L12-13,L13-14,J10-11,L11-12@2M:M10-11,M11-12,J12-13,J13-14@2M-B:M10-11,M11-12,J12-13,J13-14@3M:M12-13,M13-14.V10-11,V11-12@3M-B:M12-13,M13-14.V10-11,V11-12
105000006@ALGEBRA LINEAL@Basica@6@1@1M:L10-11,L11-12,MI12-13,MI13-14@2M:L12-13,L13-14,J10-11,J11-12@2M-B:L12-13,L13-14,J10-11,J11-12@3M:M10-11,M11-12,J12-13,J13-14@3M-B:M10-11,M11-12,J12-13,J13-14
```

## Notes
- You **can** write **uppercase and lowercase**.
- **DO  NOT use non-ASCII characters** like accents, points, commas, special symbols, ...
- **Each subject MUST be written in a single line**
