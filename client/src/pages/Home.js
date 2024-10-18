import { Box, Button, Image, Text } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";


const Home = () => {

    const navigate = useNavigate()

    const handleClickButton = () => {
        navigate("/receitas")
    }

    return (
        <Box
            display={"flex"}
            justifyContent={"center"}
            alignItems={"center"}
        >
            <Image
                width={"100%"}
                src="https://blog.consumer.com.br/wp-content/uploads/2020/09/o-que-%C3%A9-fast-food.1.jpg"
                filter="brightness(0.5)"
            />
            <Box
                display={"flex"}
                justifyContent={"center"}
                alignItems={"center"}
                position={"fixed"}
                flexDir={"column"}
                gap={10}
                top={"30%"}
            >
                <Text
                    fontSize={50}
                    color={"white"}
                    fontWeight={"bold"}

                >Um mundo de receitas!</Text>
                <Button
                    colorScheme={"orange"}
                    onClick={handleClickButton}
                >
                    Vamos lá
                </Button>
            </Box>
        </Box>
    );
}

export default Home;