# Tuxhe Engineer practice: one folder per Short under python/.

default:
    @just --list

# Run one exercise's tests: just test V001a-comprehension-parts
test video:
    cd python/{{video}} && uv run --project ../.. pytest -q -p no:cacheprovider

# Lint, types, and that every exercise's tests load (they fail until solved, so CI does not run them)
check:
    uv run ruff check .
    uv run pyright
    for d in python/*/; do (cd "$d" && uv run --project ../.. pytest -q --collect-only -p no:cacheprovider > /dev/null) || exit 1; done
    @echo "check: all green"
