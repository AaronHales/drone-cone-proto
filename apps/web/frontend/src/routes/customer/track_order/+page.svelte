<h1>Tracking Order#: ???????</h1>
<div id="order_tracking">
    <p id="time_order">Order Date: MM/DD/YYYY HH:MM</p>
    <p id="delivery_order">Delivered/Arriving: TIME</p>
    <p id="cost_order">Order Total: $?????? (# cones)</p>
</div>
<div id="content_order">
    <div id="order">
        <div id="cone">
            <p>Cone: ????</p>
            <p>Scoops:</p>
            <ul>
                <li>option</li>
                <li>option</li>
                <li>option</li>
            </ul>
            
            <p>Toppings:</p>
            <ul>
                <li>options.</li>
                <li>options.</li>
                <li>options.</li>
            </ul>
        </div>

        <div id="buttons">
            <p id="quantity">Qty. ??</p>
            <div>
                <span id="add_to_cat_icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="50" height="44" viewBox="0 0 70 63" fill="none">
                        <g clip-path="url(#clip0_2_79)">
                            <path d="M12.3364 4.95961L13.0138 6.38889H14.5955H64.5434C66.0991 6.38889 67.2267 7.86813 66.8218 9.35851L66.8203 9.36402L61.8386 27.8693C61.8384 27.8699 61.8383 27.8704 61.8381 27.871C61.0982 30.6014 58.6201 32.5 55.8055 32.5H20.7448H17.7266L18.2885 35.4654L18.9447 38.929L18.9447 38.929L18.9471 38.9413C19.4418 41.482 21.6679 43.3334 24.2691 43.3334H59.3055C59.5412 43.3334 59.7222 43.5144 59.7222 43.75C59.7222 43.9856 59.5412 44.1667 59.3055 44.1667H24.2691C21.2631 44.1667 18.6879 42.0293 18.1337 39.0935L18.133 39.0897L11.8649 6.17036C11.8643 6.16713 11.8637 6.16389 11.8631 6.16066C11.5505 4.48978 10.0941 3.33334 8.44618 3.33334H2.91667C2.68106 3.33334 2.5 3.15228 2.5 2.91667C2.5 2.68106 2.68106 2.5 2.91667 2.5H8.44618C10.1359 2.5 11.6364 3.48278 12.3364 4.95961ZM18.0556 56.3889C18.0556 55.9512 18.1418 55.5177 18.3093 55.1133C18.4768 54.7089 18.7223 54.3414 19.0319 54.0319C19.3414 53.7224 19.7089 53.4768 20.1133 53.3093C20.5177 53.1418 20.9511 53.0556 21.3889 53.0556C21.8266 53.0556 22.2601 53.1418 22.6645 53.3093C23.0689 53.4768 23.4364 53.7224 23.7459 54.0319C24.0554 54.3414 24.301 54.7089 24.4685 55.1133C24.636 55.5177 24.7222 55.9512 24.7222 56.3889C24.7222 56.8267 24.636 57.2601 24.4685 57.6645C24.301 58.069 24.0554 58.4364 23.7459 58.7459C23.4364 59.0555 23.0689 59.301 22.6645 59.4685C22.2601 59.636 21.8266 59.7223 21.3889 59.7223C20.9511 59.7223 20.5177 59.636 20.1133 59.4685C19.7089 59.301 19.3414 59.0555 19.0319 58.7459C18.7223 58.4364 18.4768 58.069 18.3093 57.6645C18.1418 57.2601 18.0556 56.8267 18.0556 56.3889ZM56.3889 53.0556C57.2729 53.0556 58.1208 53.4068 58.7459 54.0319C59.371 54.657 59.7222 55.5049 59.7222 56.3889C59.7222 57.273 59.371 58.1208 58.7459 58.7459C58.1208 59.3711 57.2729 59.7223 56.3889 59.7223C55.5048 59.7223 54.657 59.3711 54.0319 58.7459C53.4067 58.1208 53.0555 57.273 53.0555 56.3889C53.0555 55.5049 53.4067 54.657 54.0319 54.0319C54.657 53.4068 55.5048 53.0556 56.3889 53.0556Z" stroke="black" stroke-width="5"/>
                        </g>
                        <defs>
                            <clipPath id="clip0_2_79">
                            <rect width="70" height="62.2223" fill="white"/>
                            </clipPath>
                        </defs>
                    </svg>
                </span>
                <button class="add_to_cart" type="button">Add to Cart</button>
            </div>
        </div>
    </div>
</div>


<style>
    h1 {
        display: flex;
        flex-direction: column;
        justify-content: center;
        flex-shrink: 0;
        text-align: center;
    }

    #order_tracking {
        height: fit-content;
        flex-shrink: 0;
        border-radius: 22px;
        background: #D9D9D9;
        padding-left: 20px;
    }

    #order {
        display: flex;
        border-radius: 22px;
        background: #D9D9D9;
        flex-shrink: 0;
    }

    #order > #cone {
        width: 95%;
        padding-left: 20px;
        display: inline;
    }

    #buttons {
        width: 5%;
        flex-shrink: 0;
    }
    
    #buttons > p {
        padding-right: 20px;
        text-align: right;
    }

    #buttons > div {
        width: fit-content;
        display: flex;
        flex-direction: column;
        text-align: right;
        justify-content: flex-end;
    }

    #buttons > div > span {
        text-align: center;
    }

</style>