py_binary(
    name = "main",
    srcs = ["main.py"],
)

py_test(
    name = "main_test",
    srcs = ["main_test.py"],
    main = "main_test.py",
    deps = [":main"],
    size = "small",
)
