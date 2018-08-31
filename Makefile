all: deps

.PHONY: deps
deps: clean
	@go get github.com/c3systems/c3-go && \
	(cd "${GOPATH}/src/github.com/c3systems/c3-go/lib/c" && \
	make) && \
	cp "${GOPATH}/src/github.com/c3systems/c3-go/lib/c/common/hashing/hashing.so" ./lib/ && \
	cp "${GOPATH}/src/github.com/c3systems/c3-go/lib/c/common/hexutil/hexutil.so" ./lib/ && \
	cp "${GOPATH}/src/github.com/c3systems/c3-go/lib/c/common/stringutil/stringutil.so" ./lib/ && \
	cp "${GOPATH}/src/github.com/c3systems/c3-go/lib/c/config/config.so" ./lib/

.PHONY: clean
clean:
		@-find . -type f -name *.so -delete

.PHONY: test
test: test/hexutil test/hashutil

.PHONY: test/hexutil
test/hexutil:
	@python util/hexutil_test.py

.PHONY: test/hashutil
test/hashutil:
	@python util/hashutil_test.py
