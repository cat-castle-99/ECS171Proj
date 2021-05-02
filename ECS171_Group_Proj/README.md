# README.md

## Files:
- static  
    - reset.css                 # Overrides browser-default styling so our website will look the same regardless of browser  
    - style.css                 # Provides style information  
  
- templates  
    - index.html                # The static web file to be served  
- server.py                     # The Controller of our webapp-will serve the index.html page, as well as any Model files  
- README.md                   # This file  



## Current Functionality:
- Can receive user input--both a categorical entry and a numerical entry  
    - As yet, not specific to the features in our dataset
- Can return information from server.py to client-side(View)

## Todo:
- Make user input areas feature-specific
- Integrate with model  
    - parse input and pass to model file
    - read output and format so it can be passed back to client-side/View
