# Python OpenCV - Minecraft Autofisher

<strong>The Concept:</strong>

	1. Use 'mss' to grab a live screen recording.
	2. Use 'OpenCV' to process fishing bob in each frame.
	3. Use xdotool to initiate auto-clicks.
	4. Keep independent from the java-launcher (thus no mods / separate launcher necessary).


<strong>The Process: </strong>I noticed that an easy way to determine the appropriate time to catch a fish is when the red fishing bob dips beneath the water surface. As a result, the color of the bob will change from a bright red to a muddy color due to the discoloration from the water.

<strong>What the bob looks like when it is above the surface and not ready to catch a fish: </strong>
![](mini-projects/OpenCV-AutoFishBot/images/BobAboveWater.png)
