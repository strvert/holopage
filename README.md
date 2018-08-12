# holopage
holopage
## Step1
usege: `python genbin.py [input_file] [output_file]`

example: `python genbin.py example/stn.jpg example/stn.bin`  
↓`stn.jpg`↓  
![stn.jpg](https://raw.githubusercontent.com/strvworks/holopage/master/example/stn.jpg)

### output

```text:stn.bin
1111111111011000111111111110000000000000000100000100101001000110010010010100011000000000000000010000000100000000000000000000000100000000000000010000.....
```

## Step2
usege: `python genpage.py [dump_binary_textfile] [base_filename] ([page_pixel])`

example: `python genpage.py example/stn.bin example/base 512`

### output
![page0](https://raw.githubusercontent.com/strvworks/holopage/master/example/stn_page0.png)
![page1](https://raw.githubusercontent.com/strvworks/holopage/master/example/stn_page1.png)
![page2](https://raw.githubusercontent.com/strvworks/holopage/master/example/stn_page2.png)
![page3](https://raw.githubusercontent.com/strvworks/holopage/master/example/stn_page3.png)
![page4](https://raw.githubusercontent.com/strvworks/holopage/master/example/stn_page4.png)
![page5](https://raw.githubusercontent.com/strvworks/holopage/master/example/stn_page5.png)
