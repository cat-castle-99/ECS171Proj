# README.md

## Files:
- static  
    - reset.css                 # Overrides browser-default styling so our website will look the same regardless of browser  
    - style.css                 # Provides style information  
  
- templates  
    - index.html                # The static web file to be served  
- server.py                     # The Controller of our webapp-will serve the index.html page, as well as any Model files  
- Runtime.py                   # File with backend model building/functionality
- README.md                   # This file  



## Current Functionality:
- Can receive user input--both a categorical entry and a numerical entry  
    - As yet, not specific to the features in our dataset
- Can return information from server.py to client-side(View)
- Made user input areas for features
- Integrated with model  
    - parsed input and pass to model file
    - read output and formatted so it can be passed back to client-side/View
    - shows graphs for output to help user understand the model
