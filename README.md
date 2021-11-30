# Virtues translation project

## Unrpy
```cmd
for %i in (*.rpa) do (unrpa %i)
```

## Commands
```bash
# 提交
git add .
git commit - m "本次提交的注释"
git push
# 保存登录信息
git config --global credential.helper store
```

## Clean rpyc
```bash
find . -name "*.rpyc" |xargs rm -rfv
```
