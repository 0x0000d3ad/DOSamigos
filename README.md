# Introduction
 These are 'quick and dirty' scripts used to scrape images and metadata from the Nakamigos project.  Images were used in the construction of the DOSamigos by MaxCapacity.  These scripts are nowhere near production quality, but they should get you off the ground if you have similar requirements.

# Installation
 Dependencies include:

 1. eth_utils - for creating checksummed wallet addresses
 2. selenium - for downloading html data for use in nakamigos metadata processing
 3. Pillow - for image validation

 These can be installed as follows:

 `pip -r requirements.txt`

# Scripts

 The following scripts were used in the making of the DOSamigos project:

 1. `create_lists.py` - Aggregates separate whitelists together, using proper checksums on the names to deduplicate.  The final whitelists are created in the form Third Web is expecting.
 2. `create_metadata.py` - Creates the aggregated metadata to upload to Third Web
 3. `get_images.py` - Scrape Nakamigos images
 4. `get_metadata.py` - Scrape Nakamigos metadata.  This script spins up a fully emulated browser using selenity.  Then it navigates to the x2y2 page for each Nakamigo, and saves the HTML.  A later script (accidently deleted and therefore not included in this repo) scrapes the HTML for the final metadata.
 5. `images.py` - Validates images, shuffles images and metadata, verifies naming convention.

