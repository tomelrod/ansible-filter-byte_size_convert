filter\-byte\_size\_convert
=========

Filter to converte byte sizes from one unit to another.

Requirements
------------

None

Usage
-----

### Default Behavior
The default behavior is to convert the input into bytes. If the input has no suffix it will assume the input is also in bytes.
For example:
- `{{ '1K'|byte_size_convert }}` =  1024.0
- `{{ '512'|byte_size_convert }}`  =  512.0

### Additional Arguments
There are two arguments it will take. The first argument is to set what units(suffix) the input is. This option will override what is auto detected from the input.
For example:
- `{{ '2'|byte_size_convert('K') }}`  =  2048.0
- `{{ '2Kb'|byte_size_convert('K') }}`  =  2048.0

The second argument is what unit(suffix) to output should be.
For example:
- `{{ '1536'|byte_size_convert('K','M') }}`  =  1.5

The names of these arguments are unit\_in and unit\_out. This is useful if you only want to specify the output units and rely on the auto detection for the input.
For example:
- `{{ '1536K'|byte_size_convert(unit_out='M') }}`  =  1.5

### Notes on the return value

##### The return type of float
The filter returns a float, that is there will be a decimal place. If this is not desired use the round and int filters.
Examples:
- `{{ '1536'|byte_size_convert('K','M') }}`  =  1.5
- `{{ '1536'|byte_size_convert('K','M')|int }}`  =  1 (Convert straight to int, this truncates the decimal value, same result as rounding down)
- `{{ '1536'|byte_size_convert('K','M')|round|int }}`  =  2 (Round to nearest whole number then convert to int)
- `{{ '1536'|byte_size_convert('K','M')|round(method='floor')|int }}`  =  1 (Round down then convert to int)
- `{{ '1536'|byte_size_convert('K','M')|round(method='ceil')|int }}`  =  2 (Round up then convert to int)

##### The lack of a suffix
Lastly, this filter does not append a suffix of the units to the returned value. The output unit is known to whomever uses the filter so if the suffix is desired that can be added after the filter. It's not always desired to have the suffix and if it is the suffix a filter would add may not be written out the desired way.
For example:
With or without a space: "1MB" vs "1 MB"
Suffix spelling: "1M" vs "1MB" vs "1MiB"

A note on the last example. This filter does not interprets the three values given as equivalent. "1M" and "1MiB" are treated as base 2 and "1MB" as base 10. This is a reason for the "unit\_in" argument, to provide the true units the value represents in cases where the input may uses a suffix incorrectly.

Examples
----------------

To use the byte\_size\_convert filter include this role.
```
- hosts: myhost
  tasks:
    - name: Use the byte_size_convert filter
      debug:
        msg: "{{ '20G'|byte_size_convert(unit_out='M') }}"
```


License
-------

Proprietary

Author Information
------------------

thomas.elrod@va.gov
