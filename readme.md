# scratch-verify

Verify the ownership of a Scratch account.

[![PyPI Badge](https://img.shields.io/pypi/v/scratch-verify)](https://pypi.org/project/scratch-verify)

## Install

```sh
pip install scratch-verify
```

## Usage

```py
from scratch_verify import create_code, verify_code

# The user should go to https://scratch.mit.edu/projects/440710593 and provide `code`
code = create_code()

# Verify if the user provided it
is_verified = verify_code(username, code)
```

## API

### scratch_verify.create_code()

Generate a verification code for the user to provide at https://scratch.mit.edu/projects/440710593. This is just a convenience method - you can use any numerical code. Returns a 6-digit number.

```py
from scratch_verify import create_code

print(create_code())
#=> "435543"
```

### scratch_verify.verify_code(username, code, completion_timeout?)

Verify whether the user is authenticated.

#### username

Type: `string`

The username to authenticate.

#### code

Type: `string`

The code to check for.

#### completion_timeout

Type: `number`\
Default: `Infinity`

The maximum amount of seconds that can pass since the user provided the code before it is no longer accepted.

```py
from scratch_verify import verify_code

# If the user has authenticated
print(verify_code("RichieNB", "435543"))
#=> True
```

## Related

- [scratch-verify](https://github.com/Richienb/scratch-verify) - JavaScript version.
