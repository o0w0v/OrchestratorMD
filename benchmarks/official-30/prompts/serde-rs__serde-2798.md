# serde-rs__serde-2798

Repository: https://github.com/serde-rs/serde
Base commit: `1b4da41f970555e111f471633205bbcb4dadbc63`

Start from this exact base commit in a clean checkout. Fix the public issue below. Preserve existing APIs and unrelated behavior. Return a unified Git diff against the base commit. Do not consult solution PRs, later commits, reference patches, hidden evaluator tests, or another product's output.

## Issue #2777: Serializing fields from a getter method.

Is there any way to serialize a struct field using a getter method? 

```rs
#[derive(Serialize)]
struct MyStruct {
    #[serde(serialize_getter(get_value_with_prefix))]
    value: String,
}

impl MyStruct {
    fn get_value_with_prefix(&self) -> String {
        format!("prefix-{}", self.value)
    }
}
```
I have found this workaround to write a custom serializer
```rs
impl Serialize for MyStruct {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        let mut state = serializer.serialize_struct("MyStruct", 1)?;
        state.serialize_field("value", &self.get_value_with_prefix())?;
        state.end()
    }
}

```

But the problem is that I lost the functionality of other field attributes such as:
```rs
#[serde(skip_serializing_if = "Option::is_none")]
```

Is there any other approach to achieve this but still can use the other field attributes?
