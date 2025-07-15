# Deep Learning
## optimizer
- an optimizer is an algorithm that plays a crucial role in the training process. It's responsible for adjusting the weights of the network's connections to minimize the loss function and improve the model's performance.
- Here's a breakdown of how optimizers work:

    1. Forward Pass: The network receives an input, propagates it through its layers, and generates a prediction.
    2. Loss Calculation: The predicted output is compared to the actual target value (ground truth) using a loss function (e.g., binary cross-entropy for classification). This loss quantifies how "wrong" the prediction was.
    3. Backpropagation: The loss is then propagated backward through the network, calculating the gradients (slopes) of the loss function with respect to each weight in the network.
    4. Weight Update: The optimizer utilizes the gradients to update the weights of the network in a way that minimizes the loss.
- different types of optimizers, each with its own approach to weight updates. Here are some commonly used ones:

    1. Gradient Descent (GD): A fundamental optimizer that updates weights in the opposite direction of the gradient (steepest descent). It can be slow and sensitive to the learning rate (step size).
    2. Stochastic Gradient Descent (SGD): Updates weights after each training example, potentially faster than GD but can be noisy.
    3. Mini-batch Gradient Descent: Updates weights after a small batch of examples (e.g., 32 or 64) offering a balance between speed and stability compared to GD and SGD.
    4. Momentum: Addresses the issue of oscillations in gradient descent by considering the previous update direction (momentum) along with the current gradient, leading to smoother convergence.
    5. RMSprop (Root Mean Square Prop): Adapts the learning rate for each weight based on its recent squared gradients, useful for addressing diminishing gradients in some problems.
    6. Adagrad: Another adaptive learning rate optimizer that considers the historical sum of squared gradients for each weight, can suffer from excessively low learning rates later in training.
    7. Adadelta: Similar to Adagrad but addresses its limitation by using a decaying window for the squared gradients, offering a balance.
    8. Adam (Adaptive Moment Estimation): Combines the benefits of momentum and RMSprop, often considered a good default choice due to its effectiveness and ease of use.