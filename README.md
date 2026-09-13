# Ecommerce Product Visual Suite

把一张或多张产品照片整理成一套一致、可审核的电商视觉资产。Skill 会先锁定产品身份和可验证事实，再选择合适的套图模块，逐张生成图片，并输出 Manifest、文案来源和发布检查状态。

## 核心能力

- 自动选择完整标准套图的张数；用户明确指定张数时以指定数量为准。
- 以 **MUYANG common product poster template** 作为主编排模板。
- Flowith 只提供视觉语言和版式参考，不带入第三方产品、品牌、包装或宣传语。
- 支持标准主图套图、参考驱动详情页和两者组合。
- 每个模块独立生成，保持同一 SKU 的颜色、轮廓、比例、结构和包装一致。
- 未知信息保持 `pending`；生成的文字、平台尺寸和事实内容通过后置检查后才能发布。

## 默认模块

根据素材决定最小完整集合，通常包括白底主图、次主视觉、可见卖点、材质或结构细节、使用场景、多场景和使用/信任收尾。没有可读包装或用户提供的参数时，省略参数页，不猜型号、续航、材质等级、认证或性能。

## 安装到 Codex

将仓库目录复制到 Codex 的 Skills 目录：

```bash
git clone https://github.com/killfyvibecoding/-11.git ecommerce-product-visual-suite
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ecommerce-product-visual-suite "${CODEX_HOME:-$HOME/.codex}/skills/"
```

也可以构建可导入的 `.skill` 包：

```bash
python3 scripts/validate_repo.py
python3 scripts/build_skill_package.py
```

构建结果位于 `dist/ecommerce-product-visual-suite-0.1.0.skill`。在 Codex 的 Skill 导入入口选择该文件即可。

## 使用方式

在 Codex 中提供产品照片并说明用途，例如：

```text
Use $ecommerce-product-visual-suite to turn these product photos into a complete e-commerce image set. Keep unknown specifications pending and return the images, manifest, copy provenance, and QA status.
```

内置 `image_gen` 可用时优先使用它。外部渲染器只有在用户明确选择且所需凭据已经配置时才使用；不要把 API key 写入提示词、Manifest 或 Git 历史。

## 事实、版权和发布边界

- 产品照片和可读标签是产品身份与事实的来源；模板只控制视觉语言。
- 禁止把推测的参数、功效、认证、评价、前后对比或隐藏角度写成事实。
- 生成的中文包装文字和长参数表默认标记为 `needs_review`。
- 医疗、美妆、食品、儿童用品和其他受监管品类必须由品牌方或合规人员审核。
- 发布前还要核对目标平台的主图规则、比例、文字、商标、隐私和广告要求。
- 不要把客户照片、EXIF、人物信息、内部链接或本地路径提交到公共仓库。使用外部渲染器前，确认其数据传输、保留和训练政策。

## 目录

```text
SKILL.md                         Skill 入口
agents/openai.yaml               Codex 界面元数据
references/                      模块、模板、QA 和 Flowith 适配说明
examples/generic-manifest.json   脱敏 Manifest 示例
scripts/                         校验与 .skill 打包脚本
dist/                            构建出的可导入 Skill 包
```

## 许可证

本仓库核心内容采用 [MIT License](LICENSE)，允许商业使用、修改、再发布和公开使用，但必须保留版权与许可证声明。Flowith 参考文件的权利说明见 [NOTICE.md](NOTICE.md)。

## 版本

当前版本：`0.1.0`。变更记录见 [CHANGELOG.md](CHANGELOG.md)。
