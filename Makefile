
DOCKER=docker
IMGTAG=teris45/pyjedai_em:latest
IMGPATH=.
DOCKERFILE=$(IMGPATH)/Dockerfile

.PHONY: all build push


all: build push

build:
	$(DOCKER) build -f $(DOCKERFILE) $(IMGPATH) -t $(IMGTAG)

push:
	$(DOCKER) push $(IMGTAG)

