FROM mezuri/dev:base
MAINTAINER Andreas Kipf, kipf@cs.berkeley.edu

# Install Python
RUN apt-get install -y python

# Install refine-client-py
RUN apt-get install -y wget
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN git clone https://github.com/PaulMakepeace/refine-client-py.git
RUN cd refine-client-py
RUN pip install -r requirements.txt
RUN python setup.py build
RUN python setup.py install
RUN cd ..

# Install Google Refine
RUN wget https://github.com/OpenRefine/OpenRefine/releases/download/2.5/google-refine-2.5-r2407.tar.gz
RUN tar -xf google-refine-2.5-r2407.tar.gz