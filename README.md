
# HTTP Utility on GAE

* Show IP(REMOTE_ADDR) in text/plain. (mainly for ddns)
    * http://u.w5n.org/ip
    * http://httputil.appspot.com/ip
* TBD.

## Sample

    $ ruby -r'open-uri' -e 'p open("http://u.w5n.org/ip").read()'
    125.198.79.25

## License

BSD 2-Clause License

## Contact

http://twitter.com/wataken44