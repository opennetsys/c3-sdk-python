all: deps

.PHONY: deps
deps: clean
	@go get github.com/c3systems/c3-go && \
	(cd "${GOPATH}/src/github.com/c3systems/c3-go/lib/c" && \
	make) && \
	cp "${GOPATH}/src/github.com/c3systems/c3-go/lib/c/common/hashing/hashing.so" ./lib/hashing && \
	cp "${GOPATH}/src/github.com/c3systems/c3-go/lib/c/common/hexutil/hexutil.so" ./lib/hexutil && \
	cp "${GOPATH}/src/github.com/c3systems/c3-go/lib/c/config/config.so" ./lib/config

clean:
		@-find . -type f -name *.so -delete
