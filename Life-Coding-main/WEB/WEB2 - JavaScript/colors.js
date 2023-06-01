var Body = { /* '객체' 를 이용해서 코드를 잘 정리할 수 있다 */
                /* property : methods 의 구조 */
                setColor: function (color) {
                    document.querySelector('body').style.color = color;
                },
                setBackgroundColor:function (color) {
                    document.querySelector('body').style.backgroundColor = color;
                }
            }
            /*  Body 객체의 setColor property 와 같은 것!
            function BodySetColor(color) {
                document.querySelector('body').style.color = color;
            }
            */

            function nightDayHandler(self) { /* self는 this를 받는 매개변수로 사용됨 */
                /* 함수에서 this를 쓰면
                    this는 전역객체를 가리키게 된다.
                    웹브라우저에서는 this가 윈도우를 가리키게 됨!!! */
                var target = document.querySelector('body');
                if(self.value === 'night') {
                    Body.setBackgroundColor('black');
                    Body.setColor('white');
                    self.value = 'day';
                }
                else {
                    target.style.backgroundColor = 'white';
                    target.style.color = 'black';
                    self.value = 'night';
                }
            }