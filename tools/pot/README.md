# Post-Training Optimization Tool {#pot_README}

## Introduction

Post-training Optimization Tool (POT) is designed to accelerate the inference of deep learning models by applying
special methods without model retraining or fine-tuning, like post-training quantization. Therefore, the tool does not
require a training dataset or a pipeline. To apply post-training algorithms from the POT, you need:
* A floating-point precision model, FP32 or FP16, converted into the OpenVINO&trade; Intermediate Representation (IR) format
and run on CPU with the OpenVINO&trade;.
* A representative calibration dataset representing a use case scenario, for example, 300 images.

Post-training Optimization Tool provides the following key
features:

* Two post-training 8-bit quantization algorithms: fast [DefaultQuantization](openvino/tools/pot/algorithms/quantization/default/README.md) and precise [AccuracyAwareQuantization](openvino/tools/pot/algorithms/quantization/accuracy_aware/README.md).
* Compression for different hardware targets such as CPU and GPU.
* Multiple domains: Computer Vision, Natural Language Processing, Recommendation Systems, Speech Recognition.
* [API](openvino/tools/pot/api/README.md) that helps to apply optimization methods within a custom inference script written with OpenVINO Python* API.
* Symmetric and asymmetric quantization schemes. For details, see the [Quantization](openvino/tools/pot/algorithms/quantization/README.md) section.
* Per-channel quantization for Convolutional and Fully-Connected layers.
* Global optimization of post-training quantization parameters using the [Tree-Structured Parzen Estimator](openvino/tools/pot/optimization/tpe/README.md).

The tool is aimed to fully automate the model transformation process without a need to change the model on the user's side.
The POT is available only in the Intel&reg; distribution of OpenVINO&trade; toolkit and is not opensourced. For details
about the low-precision flow in OpenVINO&trade;, see the [Low Precision Optimization Guide](docs/LowPrecisionOptimizationGuide.md).

For benchmarking results collected for the models optimized with POT tool, see [INT8 vs FP32 Comparison on Select Networks and Platforms](@ref openvino_docs_performance_int8_vs_fp32).

Further documentation presumes that you are familiar with the basic Deep Learning concepts, such as model inference,
dataset preparation, model optimization, as well as with the OpenVINO&trade; toolkit and its components such 
as  [Model Optimizer](@ref openvino_docs_MO_DG_Deep_Learning_Model_Optimizer_DevGuide) 
and [Accuracy Checker Tool](@ref omz_tools_accuracy_checker_README).

## Use POT
![](docs/images/workflow.png) 

The POT provides three basic usage scenarios:
* **[Command-line interface](docs/CLI.md)**: this is the recommended path if the model from OpenVINO&trade; 
[Model Zoo](https://github.com/openvinotoolkit/open_model_zoo) or there is a valid [Accuracy Checker Tool](@ref omz_tools_accuracy_checker_README)
configuration file for the model that allows validating model accuracy using [Accuracy Checker Tool](@ref omz_tools_accuracy_checker_README).
* **[Python* API](openvino/tools/pot/api/README.md)**: it allows integrating optimization methods implemented in POT into
a Python* inference script written with [Python* API](@ref openvino_inference_engine_ie_bridges_python_docs_api_overview). 
This flow is recommended if it is not possible to use [Accuracy Checker Tool](@ref omz_tools_accuracy_checker_README)
for validation on the dedicated dataset.
* **[Deep Learning Workbench](@ref workbench_docs_Workbench_DG_Introduction) (DL Workbench)**: a web-based graphical environment 
that enables you to optimize, fine-tune, analyze, visualize, and compare performance of deep learning models.

Note: POT also supports optimization in the so-called [**Simplified mode**](@ref pot_configs_README) which is essentially a local
implementation of the POT Python API aimed at quantizing Computer Vision with simple pre-processing and inference flow. But
please note that this mode can lead to an inaccurate model after optimization due to the difference in the model preprocessing.

To get started with POT, follow the [Installation Guide](docs/InstallationGuide.md).

## See Also

* [Low Precision Optimization Guide](docs/LowPrecisionOptimizationGuide.md)
* [Post-Training Optimization Best Practices](docs/BestPractices.md)
* [POT Frequently Asked Questions](docs/FrequentlyAskedQuestions.md) 
* [INT8 Quantization by Using Web-Based Interface of the DL Workbench](https://docs.openvinotoolkit.org/latest/workbench_docs_Workbench_DG_Int_8_Quantization.html)
