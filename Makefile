#
#  Author: Hari Sekhon
#  Date: 2013-01-06 15:45:00 +0000 (Sun, 06 Jan 2013)
#

# Library dependencies are handled in one place in calling project

#ifdef TRAVIS
#    SUDO2 =
#else
#    SUDO2 = sudo
#endif
#
## EUID /  UID not exported in Make
#ifeq '$(USER)' 'root'
#    SUDO =
#    SUDO2 =
#else
#    SUDO = sudo
#endif

.PHONY: make
make:
	git update-index --assume-unchanged custom_tlds.txt
	#pip install mysql
	pip install coveralls

.PHONY: test
test:

.PHONY: install
install:
	@echo "No installation needed, just add '$(PWD)' to your \$$PATH"

.PHONY: update
update:
	git pull
	make

tld:
	wget -O tlds-alpha-by-domain.txt http://data.iana.org/TLD/tlds-alpha-by-domain.txt
