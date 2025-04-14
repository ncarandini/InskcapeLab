# Inkscape Lab
This project is the result of an half day spike to learn ho to create simple extensions in Python for the drawing app Inkscape.

# List circles
The first extension (and at the time the only one) I wrote has been designed to give me a list of center coordinates of some circles I drawn to simulate a plywood rectangle filled with holes.
The idea is to use Inkscape to adjust and rearrange the holes until a good disposition is reached. Then, to fisically drill the holes, I need know the centers coordinates.
To move from this:

![image](https://github.com/user-attachments/assets/0b516304-b128-4c81-adba-88997611b349)

to this:

![Immagine WhatsApp 2025-04-12 ore 18 36 48_4866841c](https://github.com/user-attachments/assets/ffe78720-5661-4475-8e85-a11fb8238b18)

### Usage
To use it, find where inkskape is installed and copy listcenters.inx and listcenters.py files in the Inkscape\share\extensions folder.

### Warning
Beware that Inkscape object coordinates are centered only if the object is a cirle (i.e. on rectangles the point is the lower left) and that transformations are not taken into account, so it's important to check that the layer has no trasformations and the circles are not grouped.
You can check this on the Inskape XML editor:

![image](https://github.com/user-attachments/assets/f02e2a54-b2f8-4087-84c4-5bae2f3eaa32)
