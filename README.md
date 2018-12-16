*Project is no longer maintained. Please reach out to [@mattcan](https://github.com/mattcan) if you would like to take ownership.*

# Torrent Search

Find torrents from your command line by quickly searching across a variety of tracking sites!

## What for?

I was interested in trying out the ISO Hunt API and
in developing more Python. And now we have this.

## Roadmap

1. More torrent sites

## Installation

Still an alpha product so it takes a bit to setup. Here are the
Ubuntu instructions:
~~~
sudo pip install requests beautifulsoup4
~~~

Then download `https://pypi.python.org/pypi/colorama`, extract, and install:
~~~
cd ~/Downloads
wget https://pypi.python.org/packages/source/c/colorama/colorama-0.2.5.tar.gz#md5=308c6e38917bdbfc4d3b0783c614897d
tar -xvzf colorama-0.2.5.tar.gz
cd colorama-0.2.5
sudo python setup.py install
~~~

Now clone the source:
~~~
cd ~/Sources
git clone https://github.com/mattcan/TorrentSearch.git
~~~

## Usage

Search for an Ubuntu iso?
~~~
cd ~/Sources/TorrentSearch
python main.py ubuntu
~~~
