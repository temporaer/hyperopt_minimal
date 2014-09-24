EXPKEY=test0
all:
	echo "make {server|client|show}"

server:
	python search.py search $(EXPKEY)

client:
	PYTHONPATH=`pwd` hyperopt-mongo-worker --mongo=localhost:27017/razlaw --poll-interval=0.1 --exp-key=$(EXPKEY)

show:
	python search.py history $(EXPKEY)
	python search.py histogram $(EXPKEY)
	python search.py vars $(EXPKEY)

clean:
	find -type d -name '????????????????????????' -exec rm -r {} \;
