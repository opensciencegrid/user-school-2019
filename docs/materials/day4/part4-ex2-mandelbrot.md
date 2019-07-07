---
status: done
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: \#008; } </style>

Monday Exercise 4.2: A Brief Detour Through the Mandelbrot Set
==============================================================

Before we explore using DAGs to implement workflows, let’s get a more interesting job. Let’s make pretty pictures!

We have a small program that draws pictures of the Mandelbrot set. You can [read about the Mandelbrot set on Wikipedia](https://en.wikipedia.org/wiki/Mandelbrot_set), or you can simply appreciate the pretty pictures. It’s a fractal.

We have a simple program that can draw the Mandelbrot set. It's called `goatbrot`, and you can find it on most Linux servers in `/usr/local/bin/goatbrot`.

Running goatbrot From the Command Line
--------------------------------------

You can generate the Mandelbrot set as a quick test with two simple commands.

1.  Generate a PPM image of the Mandelbrot set:

        :::console
        username@learn $ /usr/local/bin/goatbrot -i 1000 -o tile_000000_000000.ppm -c 0,0 -w 3 -s 1000,1000

    The `goatbroat` program takes several parameters. Let's break them down:

    -   `-i 1000` The number of iterations. Bigger numbers generate more accurate images but are slower to run.
    -   `-o tile_000000_000000.ppm` The output file to generate.
    -   `-c 0,0` The center point of the image. Here it is the point (0,0).
    -   `-w 3` The width of the image. Here is 3.
    -   `-s 1000,1000` The size of the final image. Here we generate a picture that is 1000 pixels wide and 1000 pixels tall.

1.  Convert the image to the JPEG format (using a built-in program called `convert`):

        :::console
        username@learn $ convert tile_000000_000000.ppm mandel.jpg

Dividing the Work into Smaller Pieces
-------------------------------------

The Mandelbrot set can take a while to create, particularly if you make the iterations large or the image size large. What if we broke the creation of the image into multiple invocations (an HTC approach!) then stitched them together? Once we do that, we can run the each goatbroat in parallel in our cluster. Here's an example you can run by hand.

1.  Run goatbroat 4 times:

        :::console
        username@learn $ /usr/local/bin/goatbrot -i 1000 -o tile_000000_000000.ppm -c -0.75,0.75 -w 1.5 -s 500,500
        username@learn $ /usr/local/bin/goatbrot -i 1000 -o tile_000000_000001.ppm -c 0.75,0.75 -w 1.5 -s 500,500 
        username@learn $ /usr/local/bin/goatbrot -i 1000 -o tile_000001_000000.ppm -c -0.75,-0.75 -w 1.5 -s 500,500 
        username@learn $ /usr/local/bin/goatbrot -i 1000 -o tile_000001_000001.ppm -c 0.75,-0.75 -w 1.5 -s 500,500

1.  Stitch the small images together into the complete image (in JPEG format):

        :::console
        username@learn $ montage tile_000000_000000.ppm tile_000000_000001.ppm tile_000001_000000.ppm tile_000001_000001.ppm -mode Concatenate -tile 2x2 mandel.jpg

This will produce the same image as above. We divided the image space into a 2×2 grid and ran `goatbrot` on each section of the grid. The built-in `montage` program simply stitches the files together and writes out the final image in JPEG format.

View the Image!
---------------

Run the commands above, make sure you can create the Mandelbrot image. 
When you create the image, you might wonder how you can view it. 
If you're comfortable with `scp` or another method, you can copy it back to your laptop to view it. Otherwise you can view it in your web browser in three easy steps:

1.  Make your web directory (you only need to do this once):

        :::console
        username@learn $ cd ~
        username@learn $ mkdir public_html 
        username@learn $ chmod 0711 . 
        username@learn $ chmod 0755 public_html

1.  Copy the image into your web directory (the below command assumes you're back in the directory where you created mandel.jpg):

        :::console
        username@learn $ cp mandel.jpg ~/public_html/

1.  Access `http://learn.chtc.wisc.edu/~%RED%<USERNAME>%ENDCOLOR%/mandel.jpg` in your web browser (change %RED%<USERNAME>%ENDCOLOR% to your username on the submit machine).


